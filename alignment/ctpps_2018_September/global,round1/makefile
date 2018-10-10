all: collect_data

collect_data: collect_data.cc
	g++ --std=c++11 -Wall -Wextra `root-config --libs` -lMinuit `root-config --cflags` -g\
		collect_data.cc -o collect_data

