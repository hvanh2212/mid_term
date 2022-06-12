BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "tickets" (
	"ticket_id"	TEXT NOT NULL,
	"ticket_name"	TEXT NOT NULL,
	"ticket_description"	TEXT NOT NULL,
	"created_time"	TEXT DEFAULT CURRENT_TIMESTAMP,
	"update_time"	TEXT,
	"status_name"	TEXT CHECK(status_name in ('New','On-going','Done')),
	"assignee_id"	TEXT,
	"assigneer_id"	TEXT,
	"category_name"	TEXT,
	"priority_name"	TEXT CHECK(priority_name in ('Low','Medium','High')),
	PRIMARY KEY("ticket_id"),
	FOREIGN KEY("assignee_id") REFERENCES "owner"("owner_id"),
	FOREIGN KEY("assigneer_id") REFERENCES "owner"("owner_id")
);
CREATE TABLE IF NOT EXISTS "owner" (
	"owner_id"	TEXT NOT NULL,
	"owner_name"	TEXT NOT NULL,
	"owner_mail"	TEXT NOT NULL,
	PRIMARY KEY("owner_id")
);
INSERT INTO "tickets" ("ticket_id","ticket_name","ticket_description","created_time","update_time","status_name","assignee_id","assigneer_id","category_name","priority_name") VALUES ('1','zoo','','2022-06-09 17:48:27',NULL,'New','1','1','dont know','Low');
INSERT INTO "owner" ("owner_id","owner_name","owner_mail") VALUES ('1','Jack','jack@gmail.com'),
 ('2','Mary','mary@gmail.com');
COMMIT;
