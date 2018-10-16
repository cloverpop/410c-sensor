
target: main

libbmm150.so : bmm150.c  bmm150_defs.h bmm150.h
	gcc -L/usr/lib/aarch64-linux-gnu -Wall -shared -o libbmm150.so bmm150.c


main: main.c libbmm150.so
	gcc -L/usr/lib/aarch64-linux-gnu -L. -Wall -o $@ main.c -lmraa -lbmm150



clean :
	rm -rf bmm150 bmm150.c~
	rm -rf libbmm150.so
	rm -rf main main.c~
