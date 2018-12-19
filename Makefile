CC      = gcc
CFLAGS  = -g
RM      = rm -f

DESTDIR ?=
PREFIX ?= /usr

default: all

all: hello
install: hello
	install -m 0755 -d $(DESTDIR)$(PREFIX)/bin
	install -m 0755 hello $(DESTDIR)$(PREFIX)/bin

hello: src/hello.c
	$(CC) $(CFLAGS) -o hello src/hello.c

clean veryclean:
	$(RM) hello
