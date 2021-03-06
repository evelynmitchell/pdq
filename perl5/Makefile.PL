#
# file : Makefile.PL
#
#  $Id: Makefile.PL,v 4.7 2015/08/23 01:09:30 pjpuglia Exp $
#
my $os = $^O;

if ( $os =~ /MSWin/ )

  {

    $IMAGE_BASE='-Wl,--image-base,0x14080000';

  }

use ExtUtils::MakeMaker;
WriteMakefile(
   'FIRST_MAKEFILE' => 'Makefile',
   'NAME' => 'pdq',
   'VERSION' => '6.2.0',
   dynamic_lib=>{'OTHERLDFLAGS' => $IMAGE_BASE},
   'OBJECT' => 'MVA_Approx.o MVA_Canon.o MVA_Solve.o PDQ_Build.o PDQ_Exact.o PDQ_Globals.o PDQ_Report.o PDQ_Utils.o PDQ_MServer.o pdq_wrap.o'
);
