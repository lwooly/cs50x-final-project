CREATE TABLE surf_spots (
    spot_id INTEGER NOT NULL,
    nickname TEXT NOT NULL,
    surfline_spot_id TEXT NOT NULL,
    PRIMARY KEY (spot_id)
);

ALTER TABLE surf_spots
ADD direction INTEGER ;

CREATE TABLE sessions (
    session_id INTEGER NOT NULL,
    datetime DATETIME NOT NULL,
    spot_id INTEGER NOT NULL,
    surf_max INTEGER NOT NULL,
    surf_min INTEGER NOT NULL,
    surf_humanRelation TEXT NOT NULL,
    primary_swell_height INTEGER NOT NULL,
    primary_swell_period INTEGER NOT NULL,
    primary_swell_direction INTEGER NOT NULL,
    wind_speed INTEGER NOT NULL,
    wind_direction INTEGER NOT NULL,
    wind_direction_type TEXT NOT NULL,
    wind_gust INTEGER NOT NULL,
    tide_height INTEGER NOT NULL,
    user_rating INTEGER NOT NULL,
    user_text TEXT,
    PRIMARY KEY (session_id)
    FOREIGN KEY (spot_id) REFERENCES surf_spots(spot_id)
);
