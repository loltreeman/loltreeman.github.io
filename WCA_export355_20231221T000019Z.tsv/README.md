# World Cube Association – Results Database Export

- Date: December 21, 2023
- Export Format Version: 1.0.0
- Contact: WCA Results Team (results@worldcubeassociation.org)
- Website: https://www.worldcubeassociation.org/results

## Description

This database export contains public information about all official WCA
competitions, WCA members, and WCA competition results.

## Goal

The goal of this database export is to provide members of the speedcubing
community a practical way to perform analysis on competition information for
statistical and personal purposes.

## Allowed Use

The information in this file may be re-published, in whole or in part, as long
as users are clearly notified of the following:

> This information is based on competition results owned and maintained by the
> World Cube Assocation, published at https://worldcubeassociation.org/results
> as of December 21, 2023.

## Acknowledgements

The WCA database was originally created and maintained by:

- Clément Gallet, France
- Stefan Pochmann, Germany
- Josef Jelinek, Czech Republic
- Ron van Bruchem, Netherlands

The database contents are now maintained by the WCA Results Team, and the
software for the database is maintained by the WCA Software Team:
https://www.worldcubeassociation.org/about

## Date and Format Version

The export contains a `metadata.json` file, with the following fields:

| Field                   | Sample Value              |
|-------------------------|---------------------------|
| `export_date`           | `"2023-12-21T00:00:19+00:00"` |
| `export_format_version` | `"1.0.0"` |

If you regularly process this export, we recommend that you check the
`export_format_version` value in your program and and review your code if the
major part of the version (the part before the first `.`) changes.

If you are processing the exported data using an automated system, we recommend
using a cron job to check the API endpoint at:
https://www.worldcubeassociation.org/api/v0/export/public
You can use the `export_date` to detect if there is a new export, and the
`sql_url` and `tsv_url` will contain the URLs for the corresponding downloads.

## Format (version 1.0.0)

The database export consists of these tables:

| Table                                   | Contents                                           |
|-----------------------------------------|----------------------------------------------------|
| Persons                                 | WCA competitors                                    |
| Competitions                            | WCA competitions                                   |
| Events                                  | WCA events (3x3x3 Cube, Megaminx, etc)             |
| Results                                 | WCA results per competition+event+round+person     |
| RanksSingle                             | Best single result per competitor+event and ranks  |
| RanksAverage                            | Best average result per competitor+event and ranks |
| RoundTypes                              | The round types (first, final, etc)                |
| Formats                                 | The round formats (best of 3, average of 5, etc)   |
| Countries                               | Countries                                          |
| Continents                              | Continents                                         |
| Scrambles                               | Scrambles                                          |
| championships                           | Championship competitions                          |
| eligible_country_iso2s_for_championship | See explanation below                              |

Most of the tables should be self-explanatory, but here are a few specific details:

### Countries

`Countries` stores include those from the Wikipedia list of countries at
http://en.wikipedia.org/wiki/List_of_countries, and may include some countries
that no longer exist. The ISO2 column should reflect ISO 3166-1 alpha-2
country codes, for countries that have them. Custom codes may be used in some
circumstances.

### Scrambles

`Scrambles` stores all scrambles.

For `333mbf`, an attempt is comprised of multiple newline-separated scrambles.
However, newlines can cause compatibility issues with TSV parsers. Therefore, in
the TSV version of the data we replace each newline in a `333mbf` scramble with
the `|` character.

