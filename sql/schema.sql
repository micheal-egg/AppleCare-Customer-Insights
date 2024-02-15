-- Table for storing survey responses
-- I will be generating customer survey data with SQL
CREATE TABLE IF NOT EXISTS surveys (
  survey_id TEXT PRIMARY KEY, -- Unique ID for each survey
  submitted_at TEXT, --  The time the customer submitted the survey
  product_line TEXT, -- Stuff like iPhone or Mac
  region TEXT,
  rating INTEGER,
  comment_raw TEXT,
  comment_clean TEXT
);

-- Table for storing analytics results
CREATE TABLE IF NOT EXISTS analytics (
  survey_id TEXT PRIMARY KEY REFERENCES surveys(survey_id), -- Foreign key to surveys table
  sentiment REAL,
  topic_label TEXT, -- Stuff like Battery Issue or Customer Service
  keyphrases TEXT,
  model_version TEXT
);

