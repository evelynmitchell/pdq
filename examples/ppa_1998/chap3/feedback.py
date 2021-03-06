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
#  $Id: feedback.py,v 4.5 2013/02/13 05:30:09 pjpuglia Exp $
#
#---------------------------------------------------------------------

import pdq

#---------------------------------------------------------------------
# Based on open_feedback

rx_prob          = 0.30
inter_arriv_rate = 0.5
service_time     = 0.75
mean_visits      = 1.0 / (1.0 - rx_prob)

#----- Initialize the model ------------------------------------------

pdq.Init("Open Feedback")


#---- Define the queueing center -------------------------------------

pdq.nodes = pdq.CreateNode("channel", pdq.CEN, pdq.FCFS)


#---- Define the workload and circuit type ---------------------------

pdq.streams = pdq.CreateOpen("message", inter_arriv_rate)


#---- Define service demand due to workload on the queueing center ---

pdq.SetVisits("channel", "message", mean_visits, service_time)


#---- Must import the CANONical method for an open circuit -----------

pdq.Solve(pdq.CANON)

pdq.Report()

#---------------------------------------------------------------------
