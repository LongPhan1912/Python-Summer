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
    /** the player's email. */
    private String playerEmail;
    /** the gameStateID of the player. */
    private int playerState;
    /** the team of the player. */
    private int playerTeam;
    /**
     * Creates a game summary from JSON from the server.
     * @param infoFromServer - one object from the array in the /games response
     */
    public GameSummary(final com.google.gson.JsonObject infoFromServer) {
        gameID = infoFromServer.get("id").getAsString();
        gameMode = infoFromServer.get("mode").getAsString();
        gameOwner = infoFromServer.get("owner").getAsString();
        gameState = infoFromServer.get("state").getAsInt();
        JsonArray players = infoFromServer.get("players").getAsJsonArray();
        for (int i = 0; i < players.size(); i++) {
            JsonObject player = players.get(i).getAsJsonObject();
            playerEmail = player.get("email").getAsString();
            System.out.println(playerEmail);
            playerState = player.get("state").getAsInt();
            playerTeam = player.get("team").getAsInt();
        }
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
        System.out.println(playerEmail);
        String[] teamNames = context.getResources().getStringArray(R.array.team_choices);
        if (playerEmail.equals(userEmail)) {
            return teamNames[playerTeam];
        }
        return null;
    }

    /**
     * Determines whether this game is an invitation to the user.
     * @param userEmail - the logged-in user's email
     * @return whether the user is invited to this game
     */
    public boolean isInvitation(final java.lang.String userEmail) {
        if (userEmail.equals(playerEmail)) {
            if (playerState != PlayerStateID.INVITED) {
                return false;
            }
        }
        return gameState != GameStateID.ENDED;
    }

    /**
     * Determines whether the user is currently involved in this game.
     * For a game to be ongoing, it must not be over and the user must have accepted their invitation to it.
     * @param userEmail - the logged-in user's email
     * @return whether this game is ongoing for the user
     */
    public boolean isOngoing(final java.lang.String userEmail) {
        if (userEmail.equals(playerEmail)) {
            if (gameState != GameStateID.ENDED) {
                return playerState != PlayerStateID.INVITED;
            }
        }
        return false;
    }
}
