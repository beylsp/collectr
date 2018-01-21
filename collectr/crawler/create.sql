-- sparkmodel table
CREATE TABLE
IF NOT EXISTS sparkmodel (
id integer PRIMARY KEY AUTOINCREMENT,
product_id text NOT NULL,
image_url text NOT NULL,
title text NOT NULL,
in_collection boolean NOT NULL
);
