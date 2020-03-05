package edu.illinois.cs.cs125.spring2020.mp;

import android.content.Intent;

import androidx.appcompat.app.AppCompatActivity;
import edu.illinois.cs.cs125.spring2020.mp.logic.GameStateID;
//import edu.illinois.cs.cs125.spring2020.mp.logic.PlayerStateID;
import edu.illinois.cs.cs125.spring2020.mp.logic.PlayerStateID;
import edu.illinois.cs.cs125.spring2020.mp.logic.WebApi;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.Toast;

import com.android.volley.Request;
import com.google.firebase.auth.FirebaseAuth;
import com.google.gson.JsonArray;
//import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

/**
 * Represents the main screen of the app, where the user can view and enter games.
 */
public final class MainActivity extends AppCompatActivity {

    /**
     * Called by the Android system when the activity is to be set up.
     * @param savedInstanceState info from the previously terminated instance (unused)
     */
    @Override
    protected void onCreate(final Bundle savedInstanceState) {
        // This "super" call is required for all activities
        super.onCreate(savedInstanceState);
        // Create the UI from a layout resource
        setContentView(R.layout.activity_main);
        // Now that setContentView has been called, findViewById can find views

        // This activity doesn't do anything yet - it immediately launches the game activity
        // It will be changed a little in Checkpoint 1 and filled out in Checkpoint 2
        connect();
        // Intents are Android's way of specifying what to do/launch
        // Here we create an Intent for launching GameActivity and act on it with startActivity
        // End this activity so that it's removed from the history
        // Otherwise pressing the back button in the game would come back to a blank screen here
        //finish();
    }
    /**
     * Populates the games lists UI with data retrieved from the server.
     * @param response parsed JSON from the server
     */
    private void setUpUi(final com.google.gson.JsonObject response) {
        // Hide any optional "loading" UI you added
        // Clear the games lists
        // Add UI chunks to the lists based on the result data
        JsonArray listOfGames = response.get("games").getAsJsonArray();
        String playerEmail = FirebaseAuth.getInstance().getCurrentUser().getEmail();
        //
        LinearLayout ongoingGroup = findViewById(R.id.ongoingGamesGroup);
        ongoingGroup.setVisibility(View.GONE);
        LinearLayout invitationsGroup = findViewById(R.id.invitationsGroup);
        invitationsGroup.setVisibility(View.GONE);
        // clear linear layouts
        LinearLayout ongoingGamesList = findViewById(R.id.ongoingGamesList);
        LinearLayout invitationsList = findViewById(R.id.invitationsList);
        ongoingGamesList.removeAllViews();
        invitationsList.removeAllViews();
        // variables to be used again
        String gameMode = "";
        //
        for (int i = 0; i < listOfGames.size(); i++) {
            JsonObject currentGame = listOfGames.get(i).getAsJsonObject();
            String gameId = currentGame.get("id").getAsString();
            int gameStatus = currentGame.get("state").getAsInt();
            String owner = currentGame.get("owner").getAsString();
            if (gameStatus == GameStateID.ENDED) {
                continue;
            }
            JsonArray listOfPlayers = currentGame.get("players").getAsJsonArray();
            for (int j = 0; j < listOfPlayers.size(); j++) {
                JsonObject player = listOfPlayers.get(j).getAsJsonObject();
                String userEmail = player.get("email").getAsString();
                // see whether the user is not the owner
                if (!userEmail.equals(playerEmail)) {
                    continue;
                }
                // determine which game state the player is in
                int state = player.get("state").getAsInt();
                // determine which team the player is on
                int playerTeam = player.get("team").getAsInt();
                String[] teamName = getResources().getStringArray(R.array.team_choices);
                String userRole = teamName[playerTeam];
                if (state == PlayerStateID.INVITED) {
                    View inviteChunk = getLayoutInflater().inflate(R.layout.chunk_invitation, invitationsList, false);
                    // populate the chunk
                    invitationsList.addView(inviteChunk);
                    invitationsGroup.setVisibility(View.VISIBLE);
                    // pressing the accept button
                    Button accept = inviteChunk.findViewById(R.id.acceptInvite);
                    accept.setVisibility(View.VISIBLE);
                    String finalGameId = gameId;
                    accept.setOnClickListener(v ->
                            WebApi.startRequest(this, WebApi.API_BASE + "/games/" + finalGameId + "/accept",
                                    Request.Method.POST, null, newResponse -> connect(), error ->
                                            Toast.makeText(this, "Oh no!", Toast.LENGTH_LONG).show()));
                    // pressing the decline button
                    Button decline = inviteChunk.findViewById(R.id.declineInvite);
                    decline.setVisibility(View.VISIBLE);
                    decline.setOnClickListener(v ->
                            WebApi.startRequest(this, WebApi.API_BASE + "/games/" + finalGameId + "/decline",
                                    Request.Method.POST, null, newResponse -> connect(), error ->
                                            Toast.makeText(this, "Oh no!", Toast.LENGTH_LONG).show()));
                } else if (state == PlayerStateID.ACCEPTED || state == PlayerStateID.PLAYING) {
                    View ongoingChunk = getLayoutInflater().inflate(R.layout.chunk_ongoing_game,
                            ongoingGamesList, false);
                    ongoingGamesList.addView(ongoingChunk);
                    ongoingGroup.setVisibility(View.VISIBLE);
                    // pressing the enter button
                    Button enter = ongoingChunk.findViewById(R.id.enterGame);
                    enter.setOnClickListener(v -> enterGame(gameId));
                    enter.setVisibility(View.VISIBLE);
                    // pressing the leave button
                    Button leave = ongoingChunk.findViewById(R.id.leaveGame);
                    if (leave != null) {
                        if (userEmail.equals(owner)) {
                            leave.setVisibility(View.GONE);
                        } else {
                            leave.setOnClickListener(v ->
                                    WebApi.startRequest(this, WebApi.API_BASE + "/games/" + gameId + "/leave",
                                            Request.Method.POST, null, newResponse -> connect(), error ->
                                                    Toast.makeText(this, "Oh no!", Toast.LENGTH_LONG).show()));
                            leave.setVisibility(View.VISIBLE);
                        }
                    }
                }
            }
        }
    }

    /**
     * Enters a game (shows the map).
     * @param gameId the ID of the game to enter
     */
    private void enterGame(final String gameId) {
        // Launch GameActivity with the game ID in an intent extra
        // Do not finish - the user should be able to come back here
        Intent intent = new Intent(this, GameActivity.class);
        intent.putExtra("game", gameId);
        startActivity(intent);
    }
    /**
     * Starts an attempt to connect to the server to fetch/refresh games.
     */
    protected void connect() {
        // Make any "loading" UI adjustments you like
        // Use WebApi.startRequest to fetch the games lists
        // In the response callback, call setUpUi with the received data
        LinearLayout ongoing = findViewById(R.id.ongoingGamesGroup);
        ongoing.setVisibility(View.GONE);
        LinearLayout invitations = findViewById(R.id.invitationsGroup);
        invitations.setVisibility(View.GONE);
        WebApi.startRequest(this, WebApi.API_BASE + "/games", this::setUpUi, error -> {
            Toast.makeText(this, "Oh no!", Toast.LENGTH_LONG).show();
        });
    }
}
