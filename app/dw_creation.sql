-- Create `bond_market_metrics` table
CREATE TABLE "bond_market_metrics" (
    "sk_market_metrics_id" SERIAL PRIMARY KEY,
    "fk_bond_id" INT REFERENCES "dim_bond" ("sk_bond_id"),
    "fk_date_id" INT REFERENCES "dim_date" ("sk_date_id"),
    "m1_month" NUMERIC,
    "m2_month" NUMERIC,
    "m3_month" NUMERIC,
    "m6_month" NUMERIC,
    "m1_year" NUMERIC,
    "m2_year" NUMERIC,
    "m3_year" NUMERIC,
    "m5_year" NUMERIC,
    "m7_year" NUMERIC,
    "m10_year" NUMERIC,
    "m20_year" NUMERIC,
    "m30_year" NUMERIC
);

-- Create `dim_bond` table
CREATE TABLE "dim_bond" (
    "sk_bond_id" SERIAL PRIMARY KEY,
    "treasury_name" VARCHAR
);

-- Create `dim_commodity` table
CREATE TABLE "dim_commodity" (
    "sk_commodity_id" SERIAL PRIMARY KEY,
    "symbol" VARCHAR,
    "name" VARCHAR,
    "currency" VARCHAR
);

-- Create `dim_date` table
CREATE TABLE "dim_date" (
    "sk_date_id" SERIAL PRIMARY KEY,
    "full_date" TIMESTAMP UNIQUE NOT NULL,
    "hour" INT,
    "day_of_week" INT,
    "day_name" VARCHAR(50),
    "day_of_month" INT,
    "day_of_year" INT,
    "week_of_year" INT,
    "month" INT,
    "month_name" VARCHAR(50),
    "quarter" INT,
    "year" INT,
    "fiscal_year" INT,
    "is_weekend" BOOLEAN,
    "am_pm" VARCHAR(2)
);

-- Create `dim_exchange` table
CREATE TABLE "dim_exchange" (
    "sk_exchange_id" SERIAL PRIMARY KEY,
    "name" VARCHAR NOT NULL,
    "symbol" VARCHAR UNIQUE NOT NULL,
    "opening_hour" VARCHAR,
    "closing_hour" VARCHAR,
    "timezone" VARCHAR
);

-- Create `dim_index` table
CREATE TABLE "dim_index" (
    "sk_index_id" SERIAL PRIMARY KEY,
    "symbol" VARCHAR,
    "name" VARCHAR,
    "currency" VARCHAR
);

-- Create `dim_stock` table
CREATE TABLE "dim_stock" (
    "sk_stock_id" SERIAL PRIMARY KEY,
    "symbol" VARCHAR,
    "company_name" VARCHAR,
    "currency" VARCHAR,
    "sector" VARCHAR,
    "cik" VARCHAR,
    "isin" VARCHAR,
    "cusip" VARCHAR,
    "industry" VARCHAR,
    "country" VARCHAR,
    "full_time_employees" INT,
    "city" VARCHAR,
    "state" VARCHAR,
    "ipo_date" TIMESTAMP,
    "beta" NUMERIC,
    "return_on_equity" NUMERIC,
    "shares_outstanding" BIGINT,
    "earnings_announcement" VARCHAR,
    "dividend_yield" NUMERIC,
    "debt_equity_ratio" NUMERIC,
    "price_to_book_ratio" NUMERIC,
    "cash_flow_per_share" NUMERIC,
    "peg_ratio" NUMERIC,
    "net_income" NUMERIC
);

-- Create `fact_market_metrics` table
CREATE TABLE "fact_market_metrics" (
    "sk_market_metrics_id" SERIAL PRIMARY KEY,
    "fk_date_id" INT REFERENCES "dim_date" ("sk_date_id"),
    "fk_exchange_id" INT REFERENCES "dim_exchange" ("sk_exchange_id"),
    "fk_commodity_id" INT REFERENCES "dim_commodity" ("sk_commodity_id"),
    "fk_index_id" INT REFERENCES "dim_index" ("sk_index_id"),
    "fk_stock_id" INT REFERENCES "dim_stock" ("sk_stock_id"),
    "symbol" VARCHAR,
    "current_price" NUMERIC,
    "beta" NUMERIC,
    "market_cap" NUMERIC,
    "volume" BIGINT,
    "eps" NUMERIC,  -- Calculated as net income (last 4 quarters) / shares outstanding
    "pe" NUMERIC,   -- Calculated as current_price / eps
    "vwap" NUMERIC
);
