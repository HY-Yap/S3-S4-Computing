CREATE TABLE "Character" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"element"	TEXT NOT NULL CHECK("element" IN ('Physical', 'Fire', 'Ice', 'Lightning', 'Wind', 'Quantum', 'Imaginary')),
	"path"	TEXT NOT NULL CHECK("path" IN ('Destruction', 'The Hunt', 'Erudition', 'Harmony', 'Nihility', 'Preservation', 'Abundance')),
	"stats"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "RelicSet" (
	"ID"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"SetEffect"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);

CREATE TABLE "Relic" (
	"ID"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"SetID"	INTEGER NOT NULL,
	"Position"	TEXT NOT NULL CHECK(Position IN ('Head', 'Body', 'Hand', 'Feet', 'Planar Sphere', 'Link Rope')),
	"Stats"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("SetID") REFERENCES "RelicSet"("ID")
);

CREATE TABLE "Equipment" (
	"CharacterID"	INTEGER NOT NULL,
	"RelicID"	INTEGER NOT NULL,
	PRIMARY KEY("CharacterID", "RelicID"),
	FOREIGN KEY("CharacterID") REFERENCES "Character"("name"),
	FOREIGN KEY("RelicID") REFERENCES "Relic"("ID")
);
