all:

files_moves_sgf: files_moves_sgf.tar.gz.partaa files_moves_sgf.tar.gz.partab
	cat *.tar.gz.* | tar xvfz -

files_moves_sgf.tar.gz.partaa:
	wget https://github.com/glandfried/moves-ogs-dataset/releases/download/v1.0/files_moves_sgf.tar.gz.partaa

files_moves_sgf.tar.gz.partab:
	wget https://github.com/glandfried/moves-ogs-dataset/releases/download/v1.0/files_moves_sgf.tar.gz.partab

