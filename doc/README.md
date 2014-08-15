# Project Strategy

Each term in the Roche CV will be mapped to an OWL class expression.
This expression will be used, via Jython scripts calling the OWL API,
either via [Brain](https://github.com/loopasam/Brain) or [owltools](https://code.google.com/p/owltools/), to generate tables
of mapped GO classes.  These tables will be in tsv format, making them
readable and editable on GitHub.  Table building and validation
(following any edits) will take place under continuous integration using Jenkins.

The resulting mapping tables will be checked by the Roche team who
will blacklist any problematic mappings and note anything they
consider to be missing.  The blacklist will be taken into account for
the final mapping.  Additional clauses will be considered in order to
bring in missing classes.

The tsv based strategy was chosen in order to keep the project lightweight and easy to manage - given the simplicity of the data.  However, if requirements become more baroque then data management should probaby be moved to a SQL DB (see [Notes on a simple DB schema](DB_schema_sketch.md))

# Unit tests

As the GO evolves, OWL entities referenced in the class expressions
used for mapping may become obsolete.  It is therefore important that
we run tests for the obsoletion status of classes referenced.

# Versioning

An iterative cycle of development, feedback, and further development
will require a versioning system that allows us to keep track of the
versions that refer to.

# Project structure

## mapping_tables

details TBA

## src

Jython code

## build

Build scripts (bash or Make) - to be run by Jenkins.

## doc


