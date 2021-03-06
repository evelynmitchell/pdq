#!/usr/bin/env python
###############################################################################
#  Copyright (C) 1994 - 2009, Performance Dynamics Company                    #
#                                                                             #
#  This software is licensed as described in the file COPYING, which          #
#  you should have received as part of this distribution. The terms           #
#  are also available at http://www.perfdynamics.com/Tools/copyright.html.    #
#                                                                             #
#  You may opt to use, copy, modify, merge, publish, distribute and/or sell   #
#  copies of the Software, and permit persons to whom the Software is         #
#  furnished to do so, under the terms of the COPYING file.                   #
#                                                                             #
#  This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY  #
#  KIND, either express or implied.                                           #
###############################################################################

#
#  $Id: shadowcpu.py,v 4.5 2013/02/13 05:30:09 pjpuglia Exp $
#
#---------------------------------------------------------------------

import pdq

#---------------------------------------------------------------------
#
# Based on shadowcpu.c
#
# Created by NJG: Fri May  3 18:41:04  2002
#
# Taken from p.254 of "Capacity Planning and Performance Modeling," 
# by Menasce, Almeida, and Dowdy, Prentice-Hall, 1994. 

PRIORITY = 1  # Turn priority on or off here


noPri = "CPU Scheduler - No Pri"
priOn = "CPU Scheduler - Pri On"

#---------------------------------------------------------------------

def GetProdU():
   pdq.Init("")

   pdq.streams = pdq.CreateClosed("Production", pdq.TERM, 20.0, 20.0)
   pdq.nodes   = pdq.CreateNode("CPU", pdq.CEN, pdq.FCFS)
   pdq.nodes   = pdq.CreateNode("DK1", pdq.CEN, pdq.FCFS)
   pdq.nodes   = pdq.CreateNode("DK2", pdq.CEN, pdq.FCFS)

   pdq.SetDemand("CPU", "Production", 0.30)
   pdq.SetDemand("DK1", "Production", 0.08)
   pdq.SetDemand("DK2", "Production", 0.10)

   pdq.Solve(pdq.APPROX) 

   return(pdq.GetUtilization("CPU", "Production", pdq.TERM))

#---------------------------------------------------------------------

if (PRIORITY):
   Ucpu_prod = GetProdU()
   msg = priOn
else:
   msg = noPri

#---------------------------------------------------------------------

pdq.Init(msg)

#---- Workloads ------------------------------------------------------

pdq.streams = pdq.CreateClosed("Production", pdq.TERM, 20.0, 20.0)
pdq.streams = pdq.CreateClosed("Developmnt", pdq.TERM, 15.0, 15.0)

#---- Nodes ----------------------------------------------------------

pdq.nodes = pdq.CreateNode("CPU", pdq.CEN, pdq.FCFS)

if (PRIORITY):
   pdq.nodes = pdq.CreateNode("shadCPU", pdq.CEN, pdq.FCFS)

pdq.nodes = pdq.CreateNode("DK1", pdq.CEN, pdq.FCFS)
pdq.nodes = pdq.CreateNode("DK2", pdq.CEN, pdq.FCFS)

#---- Service demands at each node -----------------------------------

pdq.SetDemand("CPU", "Production", 0.30)

if (PRIORITY):
   pdq.SetDemand("shadCPU", "Developmnt", 1.00/(1 - Ucpu_prod))
else:
   pdq.SetDemand("CPU", "Developmnt", 1.00)

pdq.SetDemand("DK1", "Production", 0.08)
pdq.SetDemand("DK1", "Developmnt", 0.05)

pdq.SetDemand("DK2", "Production", 0.10)
pdq.SetDemand("DK2", "Developmnt", 0.06)

#---- Import APPROX rather than EXACT to match the numbers in the book -

pdq.Solve(pdq.APPROX) 

pdq.Report()

#---------------------------------------------------------------------

