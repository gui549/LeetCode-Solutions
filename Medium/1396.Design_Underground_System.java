package Medium;

import java.util.HashMap;
import java.util.Map;

class UndergroundSystem {

    private Map<String, Route> routes;
    private Map<Integer, Passenger> currentPassengers;

    public UndergroundSystem() {
        routes = new HashMap<>();
        currentPassengers = new HashMap<>();
    }
    
    public void checkIn(int id, String stationName, int t) {
        if (!currentPassengers.containsKey(id)) {
            currentPassengers.put(id, new Passenger(stationName, t));
        }
    }
    
    public void checkOut(int id, String stationName, int t) {
        if (!currentPassengers.containsKey(id)) return;
        
        Passenger passenger = currentPassengers.get(id);
        String routeKey = passenger.checkInStation + ":" + stationName;

        if (!routes.containsKey(routeKey)) {
            routes.put(routeKey, new Route(passenger.checkInStation, stationName));
        }
        routes.get(routeKey).addTrip(passenger.checkInTime, t);
        currentPassengers.remove(id);
    }
    
    public double getAverageTime(String startStation, String endStation) {
        String routeKey = startStation + ":" + endStation;
        return routes.get(routeKey).getAverageTime();
    }
}

class Passenger {
    String checkInStation;
    int checkInTime;

    public Passenger(String checkInStation, int checkInTime) {
        this.checkInTime = checkInTime;
        this.checkInStation = checkInStation;
    }
}

class Route {
    String startStation;
    String endStation;
    int totalNumOfTrips; // ✅✅
    long totalTimeOfTrips; // ✅✅

    public Route(String startStation, String endStation) {
        this.startStation = startStation;
        this.endStation = endStation;
        this.totalNumOfTrips = 0;
        this.totalTimeOfTrips = 0;
    }

    double getAverageTime() {
        return (double) totalTimeOfTrips / totalNumOfTrips;
    }

    public void addTrip(int startTime, int endTime) {
        totalTimeOfTrips += endTime - startTime;
        totalNumOfTrips++;
    }
}