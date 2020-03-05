package edu.illinois.cs.cs125.spring2020.mp.logic;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import edu.illinois.cs.cs125.spring2020.mp.R;

/**
 * Extracts summary information about a game from JSON provided by the server.
 * One GameSummary instance corresponds to one object from the games array
 * in the response from the server's /games endpoint.
 */
public class GameSummary {
    /** game ID. */
    private String gameID;
    /** game mode. */
    private String gameMode;
    /** game owner's email. */
    private String gameOwner;
    /** game state (can be paused, running, or ended). */
    private int gameState;
    /** the JsonArray of players. */
    private JsonArray players;
    /** the JsonObject copy of infoFromServer. */
    private JsonObject serverInfo;
    /**
     * Creates a game summary from JSON from the server.
     * @param infoFromServer - one object from the array in the /games response
     */
    public GameSummary(final com.google.gson.JsonObject infoFromServer) {
        serverInfo = infoFromServer;
        gameID = infoFromServer.get("id").getAsString();
        gameMode = infoFromServer.get("mode").getAsString();
        gameOwner = infoFromServer.get("owner").getAsString();
        gameState = infoFromServer.get("state").getAsInt();
        players = serverInfo.get("players").getAsJsonArray();
    }
    /**
     * Gets the unique, server-assigned ID of this game.
     * @return the game ID
     */
    public java.lang.String getId() {
        return gameID;
    }

    /**
     * Gets the mode of this game, either area or target.
     * @return the game mode
     */
    public java.lang.String getMode() {
        return gameMode;
    }

    /**
     * Gets the owner/creator of this game.
     * @return the email of the game owner
     */
    public java.lang.String getOwner() {
        return gameOwner;
    }
    /**
     * Gets the name of the user's team/role.
     * @param userEmail - the logged-in user's email
     * @param context - an Android context (for access to resources)
     * @return the human-readable team/role name of the user in this game
     */
    public java.lang.String getPlayerRole(final java.lang.String userEmail,
                                          final android.content.Context context) {
        String[] teamNames = context.getResources().getStringArray(R.array.team_choices);
        for (int i = 0; i < players.size(); i++) {
            JsonObject player = players.get(i).getAsJsonObject();
            String playerEmail = player.get("email").getAsString();
            if (userEmail.equals(playerEmail)) {
                int team = player.get("team").getAsInt();
                return teamNames[team];
            }
        }
        return null;
    }

    /**
     * Determines whether this game is an invitation to the user.
     * @param userEmail - the logged-in user's email
     * @return whether the user is invited to this game
     */
    public boolean isInvitation(final java.lang.String userEmail) {
        for (int i = 0; i < players.size(); i++) {
            JsonObject player = players.get(i).getAsJsonObject();
            String playerEmail = player.get("email").getAsString();
            if (userEmail.equals(playerEmail)) {
                int playerState = player.get("state").getAsInt();
                if (playerState == PlayerStateID.INVITED && gameState != GameStateID.ENDED) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * Determines whether the user is currently involved in this game.
     * For a game to be ongoing, it must not be over and the user must have accepted their invitation to it.
     * @param userEmail - the logged-in user's email
     * @return whether this game is ongoing for the user
     */
    public boolean isOngoing(final java.lang.String userEmail) {
        for (int i = 0; i < players.size(); i++) {
            JsonObject player = players.get(i).getAsJsonObject();
            String playerEmail = player.get("email").getAsString();
            if (userEmail.equals(playerEmail)) {
                int playerState = player.get("state").getAsInt();
                if (playerState == PlayerStateID.ACCEPTED || playerState == PlayerStateID.PLAYING) {
                    if (gameState != GameStateID.ENDED) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
