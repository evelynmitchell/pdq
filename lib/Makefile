#
#  $Id: Makefile,v 4.8 2013/02/13 03:04:59 pjpuglia Exp $
#
#-----------------------------------------------------------

OSTYPE = $(shell uname)
MACH = $(shell uname -m)

ifeq ($(OSTYPE),CYGWIN_NT-5.1)
OSTYPE = cygwin
endif

ifeq ($(OSTYPE),solaris)
CC     = gcc
LIB    = libpdq.so
endif

OBJ     = \
	MVA_Approx.o \
	MVA_Canon.o \
	MVA_Solve.o \
	PDQ_Build.o \
	PDQ_Exact.o \
	PDQ_Globals.o \
	PDQ_MServer.o \
	PDQ_Report.o \
	PDQ_Utils.o

ifeq ($(MACH),x86_64)
CFLAGS	= -fPIC
endif

#-----------------------------------------------------------

all:	$(OBJ)
ifeq ($(OSTYPE),solaris)
	-$(CC) -G *.o -o ${LIB} -lm
else
	-ar -rv libpdq.a $(OBJ)
endif
ifeq ($(OSTYPE),cygwin)
	-ranlib libpdq.a          # Cygwin
endif

#-----------------------------------------------------------

clean:
	-/bin/rm -f *.o libpdq.a *~

#-----------------------------------------------------------

