CC ?= cc
CFLAGS += -Wall -Wextra -pedantic -O3 -std=c99

SRC = recursive.c
EXE = recursive
SHARERD_LIB = libchallenge.so

RM = /bin/rm -f

all: ${EXE} ${SHARERD_LIB}

${SHARERD_LIB}: ${SRC}
	${CC} ${CFLAGS} -DSHARED_LIB -shared -fPIC -o $@ $<

clean:
	$(RM) $(EXE) ${SHARERD_LIB}

