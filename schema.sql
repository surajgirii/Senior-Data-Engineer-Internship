CREATE TABLE IF NOT EXISTS fact_taxi_trips (
    trip_id SERIAL PRIMARY KEY,
    VendorID INT,
    pickup_dt TIMESTAMP NOT NULL,
    dropoff_dt TIMESTAMP NOT NULL,
    passenger_count INT,
    trip_distance NUMERIC(10, 2),
    fare_amount NUMERIC(10, 2),
    tip_amount NUMERIC(10, 2),
    total_amount NUMERIC(10, 2),
    trip_duration_min NUMERIC(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_pickup_dt ON fact_taxi_trips(pickup_dt);
CREATE INDEX idx_vendor_id ON fact_taxi_trips(VendorID);
