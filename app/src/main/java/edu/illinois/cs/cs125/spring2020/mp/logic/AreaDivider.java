package edu.illinois.cs.cs125.spring2020.mp.logic;

import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.LatLngBounds;

/**
 * Divides a rectangular area into identically sized, roughly square cells.
 * Each cell is given an X and Y coordinate. X increases from the west boundary toward the east boundary;
 * Y increases from south to north. So (0, 0) is the cell in the southwest corner.
 * (0, 1) is the cell just north of the southwestern corner cell.
 *
 * Instances of this class are created with a desired cell size.
 * However, it is unlikely that the area dimensions will be an exact multiple of that length,
 * so placing fully sized cells would leave a small "sliver" on the east or north side.
 * Length should be redistributed so that each cell is exactly the same size.
 * If the area is 70 meters long in one dimension and the cell size is 20 meters,
 * there will be four cells in that dimension (there's room for three full cells plus a 10m sliver),
 * each of which is 70 / 4 = 17.5 meters long.
 * Redistribution happens independently for the two dimensions,
 * so a 70x40 area would be divided into 17.5x20.0 cells with a 20m cell size.
 */

public class AreaDivider {
    /** latitude of the north boundary. */
    private double north;
    /** longitude of the east boundary. */
    private double east;
    /** latitude of the south boundary. */
    private double south;
    /** longitude of the west boundary. */
    private double west;
    /** side length of each cell. */
    private int cellSize;
    /** area divider to be used for multiple classes. */
    private AreaDivider divider;
    /** total width of the area. */
    private double areaWidth;
    /** total height of the area. */
    private double areaHeight;
    /** height of each cell. */
    private double cellHeight;
    /** width of each cell. */
    private double cellWidth;

    /**
     * Creates an AreaDivider for an area.
     * @param setNorth - latitude of the north boundary
     * @param setEast - longitude of the east boundary
     * @param setSouth - latitude of the south boundary
     * @param setWest - longitude of the east boundary
     * @param setCellSize - the requested side length of each cell, in meters
     */
    public AreaDivider(final double setNorth, final double setEast, final double setSouth,
                final double setWest, final int setCellSize) {
        north = setNorth;
        east = setEast;
        south = setSouth;
        west = setWest;
        cellSize = setCellSize;
        areaHeight = Math.abs(LatLngUtils.distance(new LatLng(south, west), new LatLng(north, west)));
        areaWidth = Math.abs(LatLngUtils.distance(new LatLng(north, west), new LatLng(north, east)));
        cellHeight = areaHeight / getYCells();
        cellWidth = areaWidth / getXCells();
    }

    /**
     * Gets the boundaries of the specified cell as a Google Maps LatLngBounds object.
     * Note that the LatLngBounds constructor takes the southwest
     * and northeast points of the rectangular region as LatLng objects.
     * @param x - the cell's x-coordinate
     * @param y - the cell's y-coordinate
     * @return the boundaries of the cell
     */
    public com.google.android.gms.maps.model.LatLngBounds getCellBounds(final int x, final int y) {
        LatLngBounds areaBounds = new LatLngBounds(new LatLng(south, west), new LatLng(north, east));
        return areaBounds;
    }

    /**
     * Gets the number of cells between the west and east boundaries.
     * @return the number of cells in the X direction
     */
    public int getXCells() {
        return (int) Math.ceil(areaWidth / cellSize);
    }

    /**
     * Gets the X coordinate of the cell containing the specified location.
     * The point is not necessarily within the area.
     * If it is not, the return value must not appear to be a valid cell index.
     * For example, returning 0 for a point even slightly west of the west boundary is not allowed.
     * @param location - the location
     * @return the x coordinate of the cell containing the lat-long point
     */
    public int getXIndex(final com.google.android.gms.maps.model.LatLng location) {
        double longitude = location.longitude;
        if (longitude >= west && longitude <= east) {
            double westToLocation = LatLngUtils.distance(new LatLng(north, west),
                    new LatLng(north, longitude));
            return (int) (westToLocation / cellWidth);
        }
        return -1;
    }

    /**
     * Gets the number of cells between the south and north boundaries.
     * @return the number of cells in the Y direction
     */
    public int getYCells() {
        return (int) Math.ceil(areaHeight / cellSize);
    }

    /**
     * Gets the Y coordinate of the cell containing the specified location.
     * The point is not necessarily within the area.
     * If it is not, the return value must not appear to be a valid cell index.
     * For example, returning 0 for a point even slightly south of the south boundary is not allowed.
     * @param location - the location
     * @return the y coordinate of the cell containing the lat-long point
     */
    public int getYIndex(final com.google.android.gms.maps.model.LatLng location) {
        double latitude = location.latitude;
        if (latitude < south || latitude > north) {
            return -1;
        }
        double southToLocation = LatLngUtils.distance(new LatLng(south, west),
                new LatLng(latitude, west));
        return (int) (southToLocation / cellHeight);
    }

    /**
     * Returns whether the configuration provided to the constructor is valid.
     * The configuration is valid if the cell size is positive the bounds delimit a region of positive area.
     * That is, the east boundary must be strictly further east than the west boundary and the north boundary
     * must be strictly further north than the south boundary.
     *
     * Due to floating-point strangeness, you may find our LatLngUtils.same function helpful
     * if equality comparison of double variables does not work as expected.
     * @return whether this AreaDivider can divide a valid area
     */
    public boolean isValid() {
        if (cellSize > 0) {
            if (!LatLngUtils.same(east, west) && !LatLngUtils.same(north, south)) {
                if (east - west > 0 && north - south > 0) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * Draws the grid to a map using solid black polylines.
     * There should be one line on each of the four boundaries of the overall area
     * and as many internal lines as necessary to divide the rows and columns of the grid.
     * Each line should span the whole width or height of the area rather than the side of just one cell.
     * For example, an area divided into a 2x3 grid would be drawn with 7 lines total:
     * 4 for the outer boundaries, 1 vertical line to divide the west half from the east half (2 columns),
     * and 2 horizontal lines to divide the area into 3 rows.
     *
     * See the provided addLine function from GameActivity for how to add a line to the map.
     * Since these lines should be black, they should not be paired with any extra "border" lines.
     * If equality comparisons of double variables do not work as expected, consider taking advantage of
     * our LatLngUtils.same function.
     * @param map - the Google map to draw on
     */
    public void renderGrid(final com.google.android.gms.maps.GoogleMap map) {
    }
}
