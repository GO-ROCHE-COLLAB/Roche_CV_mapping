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

# Project structure

## mapping_tables

details TBA

## src

Jython code

## build

Build scripts (bash or Make) - to be run by Jenkins.

## doc
