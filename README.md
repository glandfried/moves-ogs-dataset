# moves-ogs-dataset

## Repo: moves-ogs-database

The [OGS](https://online-go.com) plataform offers `.sgf` files which contains the moves made by players that played public games.
The Smart Game Format ([SGF](https://www.red-bean.com/sgf/user_guide/)) is a file format used for storing records of board games.

The first 12.000.000 `.sgf` files offered by OGS:

0. files\_moves\_sgf.tar.gz.partaa
0. files\_moves\_sgf.tar.gz.partab
 
You could find this files attached at the last release.

**Only public games have information** (i.e. only 60% of the files, around 8 millions files). This files where download around in 2018.

### Data

The most important feature stored in the files are the movement made by players, algongside context information.

An example:

```sgf
(;FF[<File Format>]
GM[<Type of Game>]
DT[<YYYY-MM-DD>]
PC[OGS: http://online-go.com/game/<Game ID>]
PB[<Black's nikename>]
PW[<White's nikename>]
BR[<Black's skill>]
WR[<White's skill>]
TM[<Total seconds to play>]
RE[<Result>]
SZ[<Size>]
KM[<Komi>]
RU[<Rules>]
;B[<1st black's move>]
;W[<1st white's move>]
;B[<2nd black's move>]
;W[<2nd white's move>]
;B...
)
```

The reported ability is not the ability they had at the time of playing but the ability they had at the time of downloading the files.

