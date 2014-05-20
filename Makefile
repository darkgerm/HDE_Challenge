CC ?= cc
CFLAGS += -Wall -Wextra -pedantic -O3 -std=c99
EXE = recursive
RM = /bin/rm -f

all: $(EXE)

clean:
	$(RM) $(EXE)

