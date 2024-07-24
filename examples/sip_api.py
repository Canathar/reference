# -*- coding: utf-8 -*-
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ sip_api.py                                                                                                                    ║
# ║                                                                                                                               ║
# ║ Document Encoding           : UTF-8, UNIX Line Terminator                                                                     ║
# ║ Document Best Viewed/Printed: Page{Legal, Landscape, 0.25in Side Margins}   Font{Monospaced Font, Normal, 10pt}               ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                       Revision History                                                        ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║  <public version id>+<local ver id>   <date>                     <Revision Type>                                              ║
# ║ NN.NN.NNaaNN.aaaaNNN+VV.vv.DOYyy.bb (dd MMM yy) - Initial Creation/Development Update/Maintenance Update                      ║
# ║                                                                                                                               ║
# ║                       1.00.xxxxx.xx (xx xxx xx) - Initial Creation {R. Davis}                                                 ║
# ║                       1.01.19516.00 (13 Jul 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added header, added reference data, added python source code encoding    ║
# ║                       1.02.19716.00 (15 Jul 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added proxy information                                                  ║
# ║                       1.03.20916.00 (27 Jul 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added additional proxy information                                       ║
# ║                                                      Added additional user information                                        ║
# ║                       1.04.21016.00 (28 Jul 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Moved user information to scenario files                                 ║
# ║                       1.05.21116.00 (29 Jul 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Re-factored UAC Invite functions                                         ║
# ║                       1.06.22116.00 (08 Aug 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Incorporated new library functions                                       ║
# ║                       1.07.22416.00 (11 Aug 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added Remote Proxy                                                       ║
# ║                       1.08.28816.00 (14 Oct 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Code Cleanup                                                             ║
# ║                       1.09.30016.00 (26 Oct 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Re-factored script to be PEP 8 Compliant (with --max-line-length=130)    ║
# ║                                                      Added logging/error handling                                             ║
# ║                       1.10.30216.00 (28 Oct 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added class to contain common components                                 ║
# ║                       1.11.30516.00 (31 Oct 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Modified class components                                                ║
# ║                       1.12.30616.00 (01 Nov 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added properties for class variables                                     ║
# ║                       1.13.30916.00 (04 Nov 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Loaded saved version from backup as 02-Nov-16 file was corrupted         ║
# ║                                                         (corruption was caused by author error during archive creation)       ║
# ║                                                      Modified method names from x_CWP_x to x_Remote_x                         ║
# ║                                                      Added CallType Enumeration, DetermineSubjectHeader Function              ║
# ║                                                      Added CallDuration, CallType, MaxCallCount, MaxSockets                   ║
# ║                                                      Added SippErrFileName, SippMsgFileName, SippTraceFileName                ║
# ║                       1.14.31216.00 (07 Nov 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Corrected output file name issue                                         ║
# ║                       1.15.31316.00 (08 Nov 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added additional Scenario variables                                      ║
# ║                                                      Added variable type descriptions to properties                           ║
# ║                       1.16.31516.00 (10 Nov 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added additional Scenario variables                                      ║
# ║  0. 0. 1 a 1. dev  1+ 1.17.32016.00 (15 Nov 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Began research into packaging for distribution                           ║
# ║                                                      Added public version identifier                                          ║
# ║  0. 0. 1 a 1. dev  4+ 1.18.32116.00 (16 Nov 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Modified imports to search hats package instead of tools dir             ║
# ║  0. 1. 0 a 1. dev xx+ 1.19.32616.00 (21 Nov 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Changed API name from callAPI to sipAPI                                  ║
# ║                                                      Added register and subscribe to API                                      ║
# ║  0. 2. 0 a 1. dev xx+ 1.20.34116.00 (06 Dec 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added additional response handlers to Subscribe                          ║
# ║  0. 3. 0 a 1. dev xx+ 2.00.34216.00 (07 Dec 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added unit tests                                                         ║
# ║  0. 3. 0 a 1. dev xx+ 2.01.34316.00 (08 Dec 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added sipAPICalls collection class                                       ║
# ║                                                      Added additional unit tests                                              ║
# ║  0. 5. 0 a 1. dev xx+ 2.02.34716.00 (12 Dec 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Added location enumeration                                               ║
# ║  0. 7. 0 a 1. dev xx+ 2.03.35516.00 (20 Dec 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Modified calls to execAPI                                                ║
# ║  0. 7. 0 a 1. dev xx+ 2.04.35616.00 (21 Dec 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Modified subscribe to support multiple notifies                          ║
# ║  0. 8. 0 a 1. dev xx+ 2.05.35716.00 (22 Dec 16) - Development Update {J. Laccone}                                             ║
# ║                                                      Modified named tuple call to include callAPI object                      ║
# ║  0. 9. 0 a 1. dev xx+ 2.06.00317.00 (03 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Corrected subscribe function documentation                               ║
# ║  0. 9. 0 a 1. dev xx+ 2.07.00517.00 (05 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added cancel/pause to invite function                                    ║
# ║  0. 9. 0 a 1. dev xx+ 2.08.00917.00 (09 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Corrected operation of cancel in invite function                         ║
# ║  0.10. 0 a 1. dev xx+ 2.09.01117.00 (11 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added capability to register with multiple proxies                       ║
# ║  0.10. 0 a 3. dev xx+ 2.10.01717.00 (17 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Modified exception handling to be Python 2/3 agnostic                    ║
# ║                                                      Removed 'flip the vip' code as it was ultimately not useful              ║
# ║  0.11. 0 a 1. dev xx+ 2.11.01917.00 (19 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Modified singleInvite_Remote_UAS method                                  ║
# ║  0.11. 0 a 1. dev xx+ 2.12.02317.00 (23 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Correct bug with call type                                               ║
# ║  0.11. 0 a 1. dev xx+ 2.13.02517.00 (25 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Fixed bug with INVITE                                                    ║
# ║  0.11. 0 a 1. dev xx+ 2.14.02617.00 (26 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Additional INVITE bug fixes                                              ║
# ║  0.11. 0 a 1. dev xx+ 2.15.02717.00 (27 Jan 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Debug of INVITE                                                          ║
# ║                                                      Corrected call type subject strings                                      ║
# ║  0.11. 0 a 1. dev xx+ 2.16.03217.00 (01 Feb 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added Auto-Answer Status to call types                                   ║
# ║  0.11. 0 a 1. dev xx+ 2.17.03317.00 (02 Feb 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added 480 as a response to an INVITE                                     ║
# ║  0.11. 0 a 1. dev xx+ 2.18.03717.00 (06 Feb 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added Capability to choose which side ends an INVITE                     ║
# ║  0.11. 0 a 1. dev xx+ 2.19.03917.00 (08 Feb 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added documentation to call types                                        ║
# ║  0.11. 0 a 3. dev xx+ 2.20.06017.00 (01 Mar 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added call rate options                                                  ║
# ║  0.13. 0 a 1. dev xx+ 2.21.06917.00 (10 Mar 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Moved unit tests to a separate file                                      ║
# ║  0.13. 0 a 1. dev xx+ 2.22.07417.00 (15 Mar 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added scenario pause to invite path                                      ║
# ║  0.14. 0 a 1. dev xx+ 2.23.18017.00 (29 Jun 17) - Development Update {A. Mezheritskiy}                                        ║
# ║                                                      Added INFO block for IC_OVR CallType                                     ║
# ║                                                      Created invite_CALL_FWD_UAS scenario                                     ║
# ║  0.14. 0 a 1. dev xx+ 2.23.18017.01 (29 Jun 17) - Development Update {A. Mezheritskiy}                                        ║
# ║                                                      CallType variables are now assigned in immediate                         ║
# ║                                                      script rather than passed in as parameters                               ║
# ║                                                      Added VOICE_MON functionality                                            ║
# ║  0.14. 0 a 1. dev xx+ 2.24.19517.01 (14 Jul 17) - Development Update {A. Mezheritskiy}                                        ║
# ║                                                      Updated invite_CWP_UAC to be in a working state                          ║
# ║  0.14. 0 a 1. dev xx+ 2.24.19817.01 (17 Jul 17) - Development Update {A. Mezheritskiy}                                        ║
# ║                                                      Made -h color code more human-readable                                   ║
# ║  0.15. 0 a 1. dev xx+ 2.25.20117.00 (20 Jul 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added local port                                                         ║
# ║                                                      Performed a spell check on this file                                     ║
# ║  0.16. 0 a 1. dev xx+ 2.25.20617.01 (25 Jul 17) - Development Update {A. Mezheritskiy}                                        ║
# ║                                                      added CALL_FWD_UAS scenario                                              ║
# ║  0.16. 0 a 1. dev xx+ 2.26.21217.00 (31 Jul 17) - Development Update {A. Mezheritskiy}                                        ║
# ║                                                      Refactored script to be PEP 8 Compliant (with --max-line-length=130)     ║
# ║                                                      Added bitmask to filter methods when registering                         ║
# ║  0.16. 0 a 1. dev xx+ 2.27.21917.00 (07 Aug 17) - Development Update {A. Mezheritskiy}                                        ║
# ║                                                      Fixed bug where program continues to run after                           ║
# ║                                                      ending call with non-200 response                                        ║
# ║  0.17. 0 a 1. dev xx+ 2.28.28517.00 (12 Oct 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Merged Arthur's changes into baseline                                    ║
# ║  0.17. 0 a 1. dev xx+ 2.29.28917.00 (16 Oct 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Further modifications to merged code                                     ║
# ║  0.17. 0 a 1. dev xx+ 2.30.29217.00 (19 Oct 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Debug of RTP transmission                                                ║
# ║  0.17. 0 a 1. dev xx+ 2.31.30517.00 (01 Nov 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Added RTP parameters                                                     ║
# ║  0.17. 0 a 1. dev xx+ 2.32.31717.00 (13 Nov 17) - Development Update {J. Laccone}                                             ║
# ║                                                      Changes to support new scriptAPI                                         ║
# ║  0.17. 0 a 1. dev xx+ 2.33.15519.xx (04 Jun 19) - Development Update {J. Laccone}                                             ║
# ║                                                      Updates and conversion to Python 3                                       ║
# ║  0.17. 0 a 1. dev xx+ 2.34.17119.xx (20 Jun 19) - Development Update {J. Laccone}                                             ║
# ║                                                      Updates to support INVITE REQUESTS more uniformly                        ║
# ║  0.17. 0 a 1. dev xx+ 2.35.17619.xx (25 Jun 19) - Development Update {J. Laccone}                                             ║
# ║                                                      Updates to receive a CANCEL after a RE-INVITE REQUEST                    ║
# ║  0.17. 0 a 1. dev xx+ 2.36.17719.xx (26 Jun 19) - Development Update {J. Laccone}                                             ║
# ║                                                      Debug of CANCEL reception after a RE-INVITE REQUEST                      ║
# ║  0.17. 0 a 1. dev xx+ 2.37.17819.xx (27 Jun 19) - Development Update {J. Laccone}                                             ║
# ║                                                      Further Debug of CANCEL reception after a RE-INVITE REQUEST              ║
# ║  0.17. 0 a 1. dev xx+ 2.38.18319.xx (02 Jul 19) - Development Update {J. Laccone}                                             ║
# ║                                                      Even Further Debug of CANCEL reception after a RE-INVITE REQUEST         ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                           Reference                                                           ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║   PEP 0 -- Index of Python Enhancement Proposals                                                                              ║
# ║   ----------------------------------------------                                                                              ║
# ║      https://www.python.org/dev/peps/                                                                                         ║
# ║                                                                                                                               ║
# ║   PEP 8 -- Style Guide For Python Code                                                                                        ║
# ║   ------------------------------------                                                                                        ║
# ║      https://www.python.org/dev/peps/pep-0008/                                                                                ║
# ║                                                                                                                               ║
# ║   PEP 257 -- Docstring Conventions                                                                                            ║
# ║   --------------------------------                                                                                            ║
# ║      https://www.python.org/dev/peps/pep-0257/                                                                                ║
# ║                                                                                                                               ║
# ║   PEP 263 -- Defining Python Source Code Encodings                                                                            ║
# ║   ------------------------------------------------                                                                            ║
# ║      https://www.python.org/dev/peps/pep-0263/                                                                                ║
# ║                                                                                                                               ║
# ║   PEP 282 -- A Logging System                                                                                                 ║
# ║   ---------------------------                                                                                                 ║
# ║      https://www.python.org/dev/peps/pep-0282/                                                                                ║
# ║                                                                                                                               ║
# ║   PEP 435 -- Adding an Enum type to the Python standard library                                                               ║
# ║   -------------------------------------------------------------                                                               ║
# ║      https://www.python.org/dev/peps/pep-0435/                                                                                ║
# ║                                                                                                                               ║
# ║   PEP 440 -- Version Identification and Dependency Specification                                                              ║
# ║   --------------------------------------------------------------                                                              ║
# ║      https://www.python.org/dev/peps/pep-0440/                                                                                ║
# ║                                                                                                                               ║
# ║   Logging Facility For Python                                                                                                 ║
# ║   ---------------------------                                                                                                 ║
# ║      https://docs.python.org/2/library/logging.html                                                                           ║
# ║                                                                                                                               ║
# ║   Doxygen Manual: Special Commands                                                                                            ║
# ║   --------------------------------                                                                                            ║
# ║      http://www.stack.nl/~dimitri/doxygen/manual/commands.html#cmd_intro                                                      ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                             Notes                                                             ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║   This file should be checked for compliance to the Python coding standard by entering the following in a terminal            ║
# ║      --- Ignore Discussed Here: https://github.com/PyCQA/pycodestyle/issues/386 ---                                           ║
# ║      pycodestyle --ignore E129 --max-line-len=132 sip_api.py                                                                  ║
# ║                                                                                                                               ║
# ║   This file should be checked for compliance to the Python document standard by entering the following in a terminal          ║
# ║      --- Ignore Discussed Here: https://github.com/PyCQA/pydocstyle/issues/141 ---                                            ║
# ║      pydocstyle --add-ignore D202 script_api.py                                                                               ║
# ║                                                                                                                               ║
# ║   This file should be checked for programming errors by entering the following in a terminal                                  ║
# ║      pylint --max-line-length=132 sip_api.py                                                                                  ║
# ║      pylint --max-line-length=132 --py3k sip_api.py                                                                           ║
# ║      NOTE: Use the command "pylint --long-help" to display the current linter configuration                                   ║
# ║                                                                                                                               ║
# ║   This file should be checked for compilation errors by entering the following in a terminal                                  ║
# ║      python2.7 -m py_compile sip_api.py                                                                                       ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                          SIP Reference                                                        ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║   A Hitchhiker's Guide to the Session Initiation Protocol (SIP)                                                               ║
# ║   -------------------------------------------------------------                                                               ║
# ║      https://tools.ietf.org/html/rfc5411                                                                                      ║
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ║   SIP: Session Initiation Protocol                                                                                            ║
# ║   --------------------------------                                                                                            ║
# ║      https://tools.ietf.org/html/rfc3261                                                                                      ║
# ║                                                                                                                               ║
# ║   Session Initiation Protocol (SIP) Basic Call Flow Examples                                                                  ║
# ║   ----------------------------------------------------------                                                                  ║
# ║      https://tools.ietf.org/html/rfc3665                                                                                      ║
# ║                                                                                                                               ║
# ║   Example Call Flows of Race Conditions in the Session Initiation Protocol (SIP)                                              ║
# ║   ------------------------------------------------------------------------------                                              ║
# ║      https://tools.ietf.org/html/rfc5407                                                                                      ║
# ║                                                                                                                               ║
# ║   Session Initiation Protocol (SIP) Usage of the Offer/Answer Model                                                           ║
# ║   -----------------------------------------------------------------                                                           ║
# ║      https://tools.ietf.org/html/rfc6337                                                                                      ║
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ║   SIP Call Flow Examples                                                                                                      ║
# ║   ----------------------                                                                                                      ║
# ║      https://www.ietf.org/proceedings/51/I-D/draft-ietf-sip-call-flows-05.txt                                                 ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                             SIP Flow                                                          ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║                        Sequence Diagram (all messages shown as coming from device, not proxy)                                 ║
# ║                     ────────────────────────────────────────────────────────────────────────────                              ║
# ║                                                                                                                               ║
# ║    Remote Device                                   This Function    Implemented In The Function: invite_remote_uac            ║
# ║                                                                                                                               ║
# ║    This Function                                   Remote Device    Implemented In The Function: invite_remote_uas            ║
# ║                                                                                                                               ║
# ║         UAC                                             UAS                                                                   ║
# ║         ─┬─                                             ─┬─                                                                   ║
# ║          │                                               │                                                                    ║
# ║          │                                               │                                                                    ║
# ║          │  [CSeq 1]  INVITE Request (w SDP Body)        │                                                                    ║
# ║       F1 ├──────────────────────────────────────────────>│ G1                                                                 ║
# ║          │ voice media format(s): 0 8 15 18 (can be all) │                                                                    ║
# ║          │                       ptime: xx               │                                                                    ║
# ║          │                                               │                                                                    ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   Provisional Responses to INVITE Request                   ║
# ║   │      │                                               │      │   ───────────────────────────────────────                   ║
# ║   │      │  [CSeq 1]       100 Response                  │      │   100 - Optional Response Message To                        ║
# ║   │ F2-1 │<──────────────────────────────────────────────┤ G2-1 │         Indicate The Call Is Trying                         ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │   180 - Optional Response Message To                        ║
# ║   │      │                                               │      │         Indicate The Call Is Ringing                        ║
# ║   │      │  [CSeq 1]       18x Response                  │      │                                                             ║
# ║   │ F2-2 │<──────────────────────────────────────────────┤ G2-2 │   183 - Optional Response Message To                        ║
# ║   │      │                                               │      │         Indicate Additional Information                     ║
# ║   │      │   (Only One Path Is Taken, Either F3 or X1)   │      │                                                             ║
# ║   ╘══════╪═══════════════════════════════════════════════╪══════╛                                                             ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   UAC Ends the Call With a CANCEL Request                   ║
# ║   │      │                                               │      │   ───────────────────────────────────────                   ║
# ║   │      │  [CSeq 1]      CANCEL Request                 │      │                                                             ║
# ║   │   X1 ├──────────────────────────────────────────────>│ Y1   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       200 Response                  │      │                                                             ║
# ║   │   X2 │<──────────────────────────────────────────────┤ Y2   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       487 Response                  │      │                                                             ║
# ║   │   X3 │<──────────────────────────────────────────────┤ Y3   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]        ACK Request                  │      │                                                             ║
# ║   │   X4 ├──────────────────────────────────────────────>│ Y4   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │               (Call Ends Here)                │      │                                                             ║
# ║   ╘══════╪═══════════════════════════════════════════════╪══════╛                                                             ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   Responses to INVITE Request                               ║
# ║   │      │                                               │      │   ───────────────────────────                               ║
# ║   │      │  [CSeq 1] 200 Response (w SDP Body)           │      │   200 - Response Message To Indicate                        ║
# ║   │ F3-1 │<──────────────────────────────────────────────┤ G3-1 │         Request Was Successful (OK)*                        ║
# ║   │      │ voice media format(s): 0 8 15 18 (can be all) │      │                                                             ║
# ║   │      │                       ptime: xx               │      │   3xx - Optional Response Message To                        ║
# ║   │      │                                               │      │         Indicate Redirection Of The Call                    ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       3xx Response                  │      │   4xx - Optional Response Message To                        ║
# ║   │ F3-2 │<──────────────────────────────────────────────┤ G3-2 │         Indicate Client Failure (UAC)                       ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │   5xx - Optional Response Message To                        ║
# ║   │      │                                               │      │         Indicate Server Failure (UAS)                       ║
# ║   │      │  [CSeq 1]       4xx Response                  │      │                                                             ║
# ║   │ F3-3 │<──────────────────────────────────────────────┤ G3-3 │   6xx - Optional Response Message To                        ║
# ║   │      │                                               │      │         Indicate Global Failure                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       5xx Response                  │      │   *   If 2xx response is received,                          ║
# ║   │ F3-4 │<──────────────────────────────────────────────┤ G3-4 │       MUST send the ACK request                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │   **  Establishment and direction of RTP media              ║
# ║   │      │                                               │      │       depends on SDP parameters matching                    ║
# ║   │      │  [CSeq 1]       6xx Response                  │      │                                                             ║
# ║   │ F3-5 │<──────────────────────────────────────────────┤ G3-5 │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]        ACK Request                  │      │                                                             ║
# ║   │   F4 ├──────────────────────────────────────────────>│ G4   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  (Bi-)Directional RTP (MAY Be) Established**  │      │                                                             ║
# ║   │      │<=============================================>│      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │(Only One Path Is Taken, Either R1, I1, F5, F7)│      │                                                             ║
# ║   ╘══════╪═══════════════════════════════════════════════╪══════╛                                                             ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   UAC Sends Re-INVITE Request                               ║
# ║   │      │                                               │      │   ───────────────────────────                               ║
# ║   │      │  [CSeq 1]  INVITE Request (w SDP Body)        │      │                                                             ║
# ║   │   R1 ├──────────────────────────────────────────────>│ S1   │                                                             ║
# ║   │      │  voice media format(s): 0 8 15 18 (only one)  │      │                                                             ║
# ║   │      │                       ptime: xx               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   └──────┼───────────────────────────────────────────────┼──────┘                                                             ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   Provisional Responses to Re-INVITE Request                ║
# ║   │      │                                               │      │   ──────────────────────────────────────────                ║
# ║   │      │  [CSeq 1]       100 Response                  │      │   100 - Optional Response Message To                        ║
# ║   │ R2-1 │<──────────────────────────────────────────────┤ S2-1 │         Indicate The Call Is Trying                         ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │   180 - Optional Response Message To                        ║
# ║   │      │                                               │      │         Indicate The Call Is Ringing                        ║
# ║   │      │  [CSeq 1]       18x Response                  │      │                                                             ║
# ║   │ R2-2 │<──────────────────────────────────────────────┤ S2-2 │   183 - Optional Response Message To                        ║
# ║   │      │                                               │      │         Indicate Additional Information                     ║
# ║   │      │   (Only One Path Is Taken, Either B1 or R3)   │      │                                                             ║
# ║   ╘══════╪═══════════════════════════════════════════════╪══════╛                                                             ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   UAS Ends the Call With a BYE Request                      ║
# ║   │      │                                               │      │   ────────────────────────────────────                      ║
# ║   │      │  [CSeq 1]        BYE Request                  │      │                                                             ║
# ║   │   B1 │<──────────────────────────────────────────────┤ C1   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       200 Response                  │      │                                                             ║
# ║   │   B2 ├──────────────────────────────────────────────>│ C2   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │   UAC Ends the Call With a CANCEL Request                   ║
# ║   │      │                                               │      │   ───────────────────────────────────────                   ║
# ║   │      │  [CSeq 1]      CANCEL Request                 │      │                                                             ║
# ║   │   B3 ├──────────────────────────────────────────────>│ C3   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       200 Response                  │      │                                                             ║
# ║   │   B4 │<──────────────────────────────────────────────┤ C4   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       487 Response                  │      │                                                             ║
# ║   │   B5 │<──────────────────────────────────────────────┤ C5   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]        ACK Request                  │      │                                                             ║
# ║   │   B6 ├──────────────────────────────────────────────>│ C6   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │               (Call Ends Here)                │      │                                                             ║
# ║   ╘══════╪═══════════════════════════════════════════════╪══════╛                                                             ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   Responses to Re-INVITE Request                            ║
# ║   │      │                                               │      │   ──────────────────────────────                            ║
# ║   │      │  [CSeq 1] 200 Response (w SDP Body)           │      │   200 - Response Message To Indicate                        ║
# ║   │ R3-1 │<──────────────────────────────────────────────┤ S3-1 │         Request Was Successful (OK)*                        ║
# ║   │      │  voice media format(s): 0 8 15 18 (only one)  │      │                                                             ║
# ║   │      │                       ptime: xx               │      │   4xx - Optional Response Message To                        ║
# ║   │      │                                               │      │         Indicate Client Failure (UAC)                       ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       4xx Response                  │      │                                                             ║
# ║   │ R3-2 │<──────────────────────────────────────────────┤ S3-2 │   *  If 2xx response is received, MUST send the ACK request ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │   ** Establishment and direction of RTP media depends       ║
# ║   │      │                                               │      │      on SDP parameters matching                             ║
# ║   │      │  [CSeq 1]        ACK Request                  │      │                                                             ║
# ║   │   R4 ├──────────────────────────────────────────────>│ S4   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  (Bi-)Directional RTP (MAY Be) Established**  │      │                                                             ║
# ║   │      │<=============================================>│      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │ (For Override Calls, Path I1 Is Taken Before) │      │                                                             ║
# ║   │      │   (Only One Path Is Taken, Either F5 or F7)   │      │                                                             ║
# ║   ╘══════╪═══════════════════════════════════════════════╪══════╛                                                             ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   Override Call Types, UAC Sends INFO Request               ║
# ║   │      │                                               │      │   ───────────────────────────────────────────               ║
# ║   │      │  [CSeq 1]       INFO Request                  │      │                                                             ║
# ║   │   I1 ├──────────────────────────────────────────────>│ J1   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       200 Response                  │      │                                                             ║
# ║   │ I2-1 │<──────────────────────────────────────────────┤ J2-1 │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       4xx Response                  │      │                                                             ║
# ║   │ I2-2 │<──────────────────────────────────────────────┤ J2-2 │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]        ACK Request                  │      │                                                             ║
# ║   │ I3-3 ├──────────────────────────────────────────────>│ J2-3 │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  (Path I1 to I3 Is Repeated Multiple Times)   │      │                                                             ║
# ║   ╘══════╪═══════════════════════════════════════════════╪══════╛                                                             ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   UAC Ends the Call With a BYE Request                      ║
# ║   │      │                                               │      │   ────────────────────────────────────                      ║
# ║   │      │  [CSeq 1]        BYE Request                  │      │                                                             ║
# ║   │   F5 ├──────────────────────────────────────────────>│ G5   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       200 Response                  │      │                                                             ║
# ║   │ F6-1 │<──────────────────────────────────────────────┤ G6-1 │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       4xx Response                  │      │                                                             ║
# ║   │ F6-2 │<──────────────────────────────────────────────┤ G6-2 │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]        ACK Request                  │      │                                                             ║
# ║   │ F6-3 ├──────────────────────────────────────────────>│ G6-3 │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │               (Call Ends Here)                │      │                                                             ║
# ║   ╘══════╪═══════════════════════════════════════════════╪══════╛                                                             ║
# ║   ┌──────┼───────────────────────────────────────────────┼──────┐   UAS Ends the Call With a BYE Request                      ║
# ║   │      │                                               │      │   ────────────────────────────────────                      ║
# ║   │      │  [CSeq 1]        BYE Request                  │      │                                                             ║
# ║   │   F7 │<──────────────────────────────────────────────┤ G7   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │  [CSeq 1]       200 Response                  │      │                                                             ║
# ║   │   F8 ├──────────────────────────────────────────────>│ G8   │                                                             ║
# ║   │      │                                               │      │                                                             ║
# ║   │      │               (Call Ends Here)                │      │                                                             ║
# ║   ╘══════╪═══════════════════════════════════════════════╪══════╛                                                             ║
# ║          │                                               │                                                                    ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""Module to provide helper functions to interact with a SIP call."""
from __future__ import absolute_import, division, print_function
import collections
import fileinput
import inspect
import logging
import re
import time

import enum
import ntplib

#from hats.db_api import DBAPI
#from hats.exec_api import sippXmlScenario
#from hats.session_api import SessionAPI

import hats.exec_api
import hats.script_api

import hats.SIPpXMLTools as sippXML

# Set the public version identifier (major.minor.micro) and the local version label
__version__ = "0.17.0a1.dev1+2.38.18319.00"

# Attach to the root logger
LOG = logging.getLogger()

HATS_SIP_PIPE = "/tmp/hats_cmd_pipe"

# Create a named tuple that can be used to store the parameters necessary for SIPp scripts
SippXmlScenario = collections.namedtuple('SippXmlScenario', 'call file remoteuser backup')

# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                      ===== Utility Functions =====                                            ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     determine_subject_header                                                                                              ║
# ║                                                                                                                               ║
# ║ @brief  Function to convert enumerated CallType value to header string                                                        ║
# ║                                                                                                                               ║
# ║ @param  call_type - Enumerated value denoting the type of call with which to retreive a subject header                        ║
# ║                                                                                                                               ║
# ║ @return String value representing the subject header                                                                          ║
# ║                                                                                                                               ║
# ║ @note   The call type values denoted in this function are obtained from the getSIPSubjectStrFromCallType function             ║
# ║         in SIPUtils.cpp.                                                                                                      ║
# ║                                                                                                                               ║
# ║         The subject header string values *MUST* match the const char string values in CallParam.h                             ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
def determine_subject_header(call_type):
    """Function to convert enumerated CallType value to header string."""

    fname = str(inspect.currentframe().f_code.co_name)
    LOG.debug("%s Entering", fname)

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                    A/G Call Control Call Types                                 ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    # Call-Type: SL_AG   Internal-Subject: radioCall   Const-Char-String: radio   Auto-Answer: Yes
    if call_type == CallType.AG:
        subject_header = "radio"

    # Call-Type: SL_AG_EMERGENCY   Internal-Subject: emergencyRadioCall   Const-Char-String: radio   Auto-Answer: Yes
    elif call_type == CallType.AG_EMERGENCY:
        subject_header = "radio"

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                  Special Call Control Call Types                               ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    # Call-Type: SL_IP_CONR   Internal-Subject: conrCall   Const-Char-String: CONR Call   Auto-Answer: Yes
    elif call_type == CallType.IP_CONR:
        subject_header = "CONR Call"

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                 G/G DA/IDA Call Control Call Types                             ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    # Call-Type: SL_CONF_MEETME   Internal-Subject: meetmeConfCall   Const-Char-String: Meet Me Conference Call   Auto-Answer: *
    elif call_type == CallType.CONF_MEETME:
        subject_header = "Meet Me Conference Call"

    # Call-Type: SL_IC_CHIME   Internal-Subject: DAIDACall   Const-Char-String: DA/IDA Call   Auto-Answer: No
    elif call_type == CallType.IC_CHIME:
        subject_header = "DA/IDA Call"

    # Call-Type: SL_IP_CHIME   Internal-Subject: interphoneCall   Const-Char-String: Interphone Call   Auto-Answer: No
    elif call_type == CallType.IP_CHIME:
        subject_header = "Interphone Call"

    # Call-Type: SL_MD_CHIME   Internal-Subject: DAIDAMDConfCall   Const-Char-String: MD DA/IDA Call   Auto-Answer: No
    elif call_type == CallType.MD_CHIME:
        subject_header = "MD DA/IDA Call"

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                G/G MD Voice Call Control Call Types                            ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    # Call-Type: SL_MD_VOICE   Internal-Subject: voiceMDConfCall   Const-Char-String: MD Voice Call   Auto-Answer: *
    elif call_type == CallType.MD_VOICE:
        subject_header = "MD Voice Call"

    # ========== G/G Preset Conference Control Call Types ==========

    # Call-Type: SL_CONF_PRESET   Internal-Subject: presetConfCall   Const-Char-String: Preset Conference Call   Auto-Answer: No
    elif call_type == CallType.CONF_PRESET:
        subject_header = "Preset Conference Call"

    # ========== G/G IC Voice Control Call Types ==========

    # Call-Type: SL_IC_VOICE   Internal-Subject: icVoiceCall   Const-Char-String: Voice Call   Auto-Answer: *
    elif call_type == CallType.IC_VOICE:
        subject_header = "Voice Call"

    # ========== G/G Voice Control Call Types ==========

    # Call-Type: SL_IP_VOICE   Internal-Subject: voicePageCall   Const-Char-String: Voice Page Call   Auto-Answer: *
    elif call_type == CallType.IP_VOICE:
        subject_header = "Voice Page Call"

    # ========== G/G OVR Control Call Types ==========

    # Call-Type: SL_IC_OVR   Internal-Subject: voiceOverrideCall   Const-Char-String: Override Call   Auto-Answer: Yes
    elif call_type == CallType.IC_OVR:
        subject_header = "Override Call"

    # Call-Type: SL_IP_OVR   Internal-Subject: ipOverrideCall   Const-Char-String: IP Override   Auto-Answer: Yes
    elif call_type == CallType.IP_OVR:
        subject_header = "IP Override"

    # Call-Type: SL_MD_OVR   Internal-Subject: overRideMDConfCall   Const-Char-String: MD OVR Call    Auto-Answer: Yes
    elif call_type == CallType.MD_OVR:
        subject_header = "MD OVR Call"

    # ========== G/G VM Control Call Types ==========

    # Call-Type: SL_VOICE_MON   Internal-Subject: voiceMonitoringCall   Const-Char-String: monitoring   Auto-Answer: *
    elif call_type == CallType.VOICE_MON:
        subject_header = "monitoring"

    # ========== G/G Conf Progressive Control Call Types ==========

    # Call-Type: SL_CONF_PROGRESSIVE   Internal-Subject: progConferenceCall   Const-Char-String: Broadcast   Auto-Answer: **
    elif call_type == CallType.CONF_PROGRESSIVE:
        subject_header = "Broadcast"

    # ========== G/G Misc. Call Types ==========

    # Call-Type: SL_UAS   Internal-Subject: uasCall   Const-Char-String: UAS Call   Auto-Answer: *
    elif call_type == CallType.UAS:
        subject_header = "UAS Call"

    else:
        subject_header = "unknown"

    LOG.debug("%s Exiting", fname)
    return subject_header

# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                         ===== Enumerations =====                                              ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @class  CallType                                                                                                              ║
# ║                                                                                                                               ║
# ║ @brief  Enumeration to represent all the choices available for a SIP call                                                     ║
# ║                                                                                                                               ║
# ║ @note   Values are taken from the SL_ATC_IP_CallType enumeration in ATCoIPComm.h                                              ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
class CallType(enum.Enum):
    """I am a temporary docstring."""

    AG = 1
    AG_EMERGENCY = 2

    CONF_MEETME = 10
    CONF_PRESET = 11
    CONF_PROGRESSIVE = 12

    IC_CHIME = 20
    IC_OVR = 21
    IC_VOICE = 22

    IP_CHIME = 30
    IP_CONR = 31
    IP_OVR = 32
    IP_VOICE = 33

    MD_CHIME = 40
    MD_OVR = 41
    MD_VOICE = 42

    UAS = 50

    VOICE_MON = 60

    UNKNOWN = 999


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @class    Methods                                                                                                             ║
# ║                                                                                                                               ║
# ║ @brief    Enumeration to represent all the choices available in the 'Allow' header of a SIP request                           ║
# ║                                                                                                                               ║
# ║ @note     Built to allow for bit masking operations to determine which methods are to be used (All Methods: 32767)            ║
# ║                                                                                                                               ║
# ║ @example                                                                                                                      ║
# ║           import hats.sipAPI                                                                                                  ║
# ║                                                                                                                               ║
# ║           fred = hats.sipAPI.sipAPI()                                                                                         ║
# ║                                                                                                                               ║
# ║           # Direct number entry                                                                                               ║
# ║           fred.allowMethods = 16383                                                                                           ║
# ║           fred.getAllowMethods()                                                                                              ║
# ║                                                                                                                               ║
# ║           # Single enumerated value entry                                                                                     ║
# ║           fred.allowMethods = hats.sipAPI.Methods.NOTIFY                                                                      ║
# ║           fred.getAllowMethods()                                                                                              ║
# ║                                                                                                                               ║
# ║           # Multiple enumerated value entry                                                                                   ║
# ║           fred.allowMethods = hats.sipAPI.Methods.NOTIFY | hats.sipAPI.Methods.MESSAGE                                        ║
# ║           fred.getAllowMethods()                                                                                              ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
class Methods(enum.IntEnum):
    """I am a temporary docstring."""

    INVITE = 1
    CANCEL = 2
    ACK = 4
    BYE = 8
    INFO = 16
    OPTIONS = 32
    UPDATE = 64
    REGISTER = 128
    MESSAGE = 256
    SUBSCRIBE = 512
    NOTIFY = 1024
    PRACK = 2048
    REFER = 4096
    PUBLISH = 8192
    OTHER = 16384






class SipPipelineActions(enum.IntEnum):
    """I am a temporary docstring."""

    CHECK_POINT_CALL_ME = 1

    CHECK_POINT_RINGING = 10

    UNKNOWN = 999

# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                        ===== Utility Classes =====                                            ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @class  SipAPICalls                                                                                                           ║
# ║                                                                                                                               ║
# ║ @brief  Class that pythonically extends the MutableSequence abstract base class to contain a collection of SipAPI objects     ║
# ║                                                                                                                               ║
# ║ @ref    http://blog.andrebarbosa.co/a-pythonic-collection/                                                                    ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
class SipAPICalls(collections.MutableSequence):
    """I am a temporary docstring."""

    def __init__(self, *args):
        """I am a temporary docstring."""

        fname = str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        self.data = list()
        self.extend(list(args))

        LOG.debug("%s Exiting", fname)

    def __delitem__(self, index):
        """I am a temporary docstring."""
        del self.data[index]

    def __getitem__(self, index):
        """I am a temporary docstring."""
        return self.data[index]

    def __len__(self):
        """I am a temporary docstring."""
        return len(self.data)

    def __setitem__(self, index, value):
        """I am a temporary docstring."""
        self.data[index] = value

    def __str__(self):
        """I am a temporary docstring."""
        return str(self.data)

    def insert(self, index, value):
        """I am a temporary docstring."""
        self.data.insert(index, value)



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                        ===== Object Classes =====                                             ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @class  sipAPI                                                                                                                ║
# ║                                                                                                                               ║
# ║ @brief  Class containing all the building blocks necessary to create a call scenario. The scenarios can range from the basic  ║
# ║         to the advanced based on the way the blocks are added together                                                        ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
class SipAPI(object):
    """I am a temporary docstring."""

    # Constructor
    def __init__(self, script=None):
        """I am a temporary docstring."""

        fname = 'SipAPI.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        if not script is None:
            self.__parent_script = script

        # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
        # ║                                   Script Information (Local)                               ║
        # ╠════════════════════════════════════════════════════════════════════════════════════════════╣
        # ║                                                                                            ║
        # ║   The local user is the script that is executing locally. The address data as well as      ║
        # ║   the domain and user information will change according to the test parameters.            ║
        # ║                                                                                            ║
        # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
        self.__local_site_loc = hats.script_api.ScriptLoc.UNKNOWN
        self.__local_ip = ""
        self.__local_port = 0
        self.__local_uri = ""
        self.__local_user = ""
        self.__local_user_domain = ""

        # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
        # ║                                    Device Information (Remote)                             ║
        # ╠════════════════════════════════════════════════════════════════════════════════════════════╣
        # ║                                                                                            ║
        # ║   The remote user is the device that is on the other side of the call from the locally     ║
        # ║   executing script. The address data as well as the domain and user information will       ║
        # ║   change according to the test parameters.                                                 ║
        # ║                                                                                            ║
        # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
        self.__remote_site_loc = hats.script_api.ScriptLoc.UNKNOWN
        self.__remote_ip = ""
        self.__remote_password = ""
        self.__remote_sip_user = ""
        self.__remote_uri = ""
        self.__remote_user = ""
        self.__remote_user_domain = ""

        # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
        # ║                                          Proxy Information                                 ║
        # ╠════════════════════════════════════════════════════════════════════════════════════════════╣
        # ║                                                                                            ║
        # ║   The local and remote proxies are the gateways for all calls. The local proxy is the      ║
        # ║   proxy within the scripts domain and the remote proxy is the proxy within the remote      ║
        # ║   devices domain.                                                                          ║
        # ║                                                                                            ║
        # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
        self.__local_proxy_ip = ""
        self.__local_proxy_password = ""
        self.__local_backup_proxy_ip = ""
        self.__local_backup_proxy_password = ""
        self.__remote_proxy_ip = ""
        self.__remote_proxy_password = ""

        # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
        # ║                                     Scenario Information                                   ║
        # ╠════════════════════════════════════════════════════════════════════════════════════════════╣
        # ║                                                                                            ║
        # ║   Parameters used by SIPp to control the execution of the scenario.                        ║
        # ║                                                                                            ║
        # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
        # Common Scenario Options
        self.__call_additional_header = {}
        self.__call_duration = 5000
        self.__call_end_pause = 5000
        self.__call_info_body = " "
        self.__call_timing_delta = 0
        self.__call_type = CallType.IC_VOICE

        self.__scenario_file = None
        self.__scenario_name = "default_scenario"
        self.__scenario_timeout = 30000

        # Common Response Options
        self.__response_client_error_timeout = 5000
        self.__response_normal_timeout = 20000
        self.__response_provisional_timeout = 5000
        self.__response_server_error_timeout = 5000

        # ALLOW Options
        self.__allow_methods = 16383

        # Initial INVITE Request Completion Options
        self.__initial_invite_uac_bye = False
        self.__initial_invite_uas_bye = False
        self.__initial_invite_uac_cancel = False

        # Initial INVITE Response Options
        self.__initial_invite_response_code = "200"
        self.__server_initial_response_delay = 0

        # Follow-up INVITE Request Completion Options
        self.__follow_up_invite_uac_bye = False
        self.__follow_up_invite_uas_bye = False
        self.__follow_up_invite_uac_cancel = False

        # Follow-up INVITE Response Options
        self.__follow_up_invite_response_code = "200"
        self.__server_follow_up_response_delay = 0

        # NOTIFY Options
        self.__notify_response_code = "200"

        # REGISTER Options
        self.__register_multi_proxies = False
        self.__registration_expires_time = "300"

        # SUBSCRIBE Options
        self.__subscribe_event = "Fake"
        self.__subscribe_expires_time = "120"

        # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
        # ║                SIP/SDP Media Description Configuration Variables: RTP                      ║
        # ╠════════════════════════════════════════════════════════════════════════════════════════════╣
        # ║                                                                                            ║
        # ║   Parameters used to configure the media desc RTP stream.                                  ║
        # ║                                                                                            ║
        # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
        self.__media_desc_one_rtp_port = -100
        self.__media_desc_one_rtp_port_max = 55000
        self.__media_desc_one_rtp_port_min = 50000

        self.__media_desc_one_rtp_repeat = 5

        self.__media_desc_one_rtp_source = None

        LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                                           ║
    # ║                                            ===== Class Member get Functions =====                                         ║
    # ║                                                                                                                           ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                Call Processing get Functions                                              ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_parent_script(self):
        """Get Function."""
        return self.__parent_script

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                              Script (Local) Variables get Functions                                       ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_local_site_loc(self):
        """I am a temporary docstring."""
        return self.__local_site_loc

    def __get_local_ip(self):
        """I am a temporary docstring."""
        return self.__local_ip

    def __get_local_port(self):
        """I am a temporary docstring."""
        return self.__local_port

    def __get_local_user(self):
        """I am a temporary docstring."""
        return self.__local_user

    def __get_local_user_domain(self):
        """I am a temporary docstring."""
        return self.__local_user_domain

    def __get_local_uri(self):
        """I am a temporary docstring."""

        if self.__local_uri == "":
            self.__local_uri = self.__local_user + "@" + self.__local_user_domain

        return self.__local_uri

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                  Device Information get Functions                                         ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_remote_site_loc(self):
        """I am a temporary docstring."""
        return self.__remote_site_loc

    def __get_remote_ip(self):
        """I am a temporary docstring."""
        return self.__remote_ip

    def __get_remote_password(self):
        """I am a temporary docstring."""
        return self.__remote_password

    def __get_remote_sip_user(self):
        """I am a temporary docstring."""
        return self.__remote_sip_user

    def __get_remote_user(self):
        """I am a temporary docstring."""
        return self.__remote_user

    def __get_remote_user_domain(self):
        """I am a temporary docstring."""

        if self.__remote_user_domain == "":
            self.__remote_user_domain = hats.script_api.determine_domain_from_loc(self.remote_site_loc)

        return self.__remote_user_domain

    def __get_remote_uri(self):
        """I am a temporary docstring."""

        if self.__remote_uri == "":
            self.__remote_uri = self.remote_user + "@" + self.remote_user_domain

        return self.__remote_uri

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                  Proxy Information get Functions                                          ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_local_proxy_ip(self):
        """I am a temporary docstring."""
        return self.__local_proxy_ip

    def __get_local_proxy_password(self):
        """I am a temporary docstring."""
        return self.__local_proxy_password

    def __get_local_backup_proxy_ip(self):
        """I am a temporary docstring."""
        return self.__local_backup_proxy_ip

    def __get_local_backup_proxy_password(self):
        """I am a temporary docstring."""
        return self.__local_backup_proxy_password

    def __get_remote_proxy_ip(self):
        """I am a temporary docstring."""
        return self.__remote_proxy_ip

    def __get_remote_proxy_password(self):
        """I am a temporary docstring."""
        return self.__remote_proxy_password

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                Scenario Information get Functions                                         ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                            Common Scenario get Functions                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_call_additional_header(self):
        """I am a temporary docstring."""
        return self.__call_additional_header

    def __get_call_duration(self):
        """I am a temporary docstring."""
        return self.__call_duration

    def __get_call_end_pause(self):
        """I am a temporary docstring."""
        return self.__call_end_pause

    def __get_call_info_body(self):
        """I am a temporary docstring."""
        return self.__call_info_body

    def __get_call_timing_delta(self):
        """I am a temporary docstring."""
        return self.__call_timing_delta

    def __get_call_type(self):
        """I am a temporary docstring."""
        return self.__call_type

    def __get_scenario_file(self):
        """I am a temporary docstring."""
        return self.__scenario_file

    def __get_scenario_name(self):
        """I am a temporary docstring."""
        return self.__scenario_name

    def __get_scenario_timeout(self):
        """I am a temporary docstring."""
        return self.__scenario_timeout

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                              Common Response get Functions                                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_response_client_error_timeout(self):
        """I am a temporary docstring."""
        return self.__response_client_error_timeout

    def __get_response_normal_timeout(self):
        """I am a temporary docstring."""
        return self.__response_normal_timeout

    def __get_response_provisional_timeout(self):
        """I am a temporary docstring."""
        return self.__response_provisional_timeout

    def __get_response_server_error_timeout(self):
        """I am a temporary docstring."""
        return self.__response_server_error_timeout

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                   Allow get Functions                                          ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_allow_methods(self):
        """I am a temporary docstring."""

        # Return value containing the 'Allow' request header content
        allowed = ""

        # If the bit mask doesn't allow any methods, return an empty string
        if self.__allow_methods == 0:
            return allowed

        # Grab the bit mask
        allow_bit_mask = self.__allow_methods

        # Parse the bit mask and determine what we want to allow
        for method in Methods:

            # If the bit is set, add the method to the allowed list
            if allow_bit_mask & method.value:
                allowed += method.name + ", "

        # Remove the trailing comma and space
        return allowed[:-2]

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                Initial INVITE get Functions                                    ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_initial_invite_uac_bye(self):
        """I am a temporary docstring."""
        return self.__initial_invite_uac_bye

    def __get_initial_invite_uas_bye(self):
        """I am a temporary docstring."""
        return self.__initial_invite_uas_bye

    def __get_initial_invite_uac_cancel(self):
        """I am a temporary docstring."""
        return self.__initial_invite_uac_cancel

    def __get_initial_invite_response_code(self):
        """I am a temporary docstring."""
        return self.__initial_invite_response_code

    def __get_server_initial_response_delay(self):
        """I am a temporary docstring."""
        return self.__server_initial_response_delay

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                               Follow Up INVITE get Functions                                   ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_follow_up_invite_uac_bye(self):
        """I am a temporary docstring."""
        return self.__follow_up_invite_uac_bye

    def __get_follow_up_invite_uas_bye(self):
        """I am a temporary docstring."""
        return self.__follow_up_invite_uas_bye

    def __get_follow_up_invite_uac_cancel(self):
        """I am a temporary docstring."""
        return self.__follow_up_invite_uac_cancel

    def __get_follow_up_invite_response_code(self):
        """I am a temporary docstring."""
        return self.__follow_up_invite_response_code

    def __get_server_follow_up_response_delay(self):
        """I am a temporary docstring."""
        return self.__server_follow_up_response_delay

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                     NOTIFY get Functions                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_notify_response_code(self):
        """I am a temporary docstring."""
        return self.__notify_response_code

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                    REGISTER get Functions                                      ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_register_multi_proxies(self):
        """I am a temporary docstring."""
        return self.__register_multi_proxies

    def __get_registration_expires_time(self):
        """I am a temporary docstring."""
        return self.__registration_expires_time

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                   SUBSCRIBE get Functions                                      ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_subscribe_event(self):
        """I am a temporary docstring."""
        return self.__subscribe_event

    def __get_subscribe_expires_time(self):
        """I am a temporary docstring."""
        return self.__subscribe_expires_time

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                              SIP/SDP Media Description RTP get Functions                                  ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_media_desc_one_rtp_port(self):
        """I am a temporary docstring."""
        return self.__media_desc_one_rtp_port

    def __get_media_desc_one_rtp_port_max(self):
        """I am a temporary docstring."""
        return self.__media_desc_one_rtp_port_max

    def __get_media_desc_one_rtp_port_min(self):
        """I am a temporary docstring."""
        return self.__media_desc_one_rtp_port_min

    def __get_media_desc_one_rtp_repeat(self):
        """I am a temporary docstring."""
        return self.__media_desc_one_rtp_repeat

    def __get_media_desc_one_rtp_source(self):
        """I am a temporary docstring."""
        return self.__media_desc_one_rtp_source

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                                           ║
    # ║                                            ===== Class Member set Functions =====                                         ║
    # ║                                                                                                                           ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                 Call Processing set Functions                                             ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_parent_script(self, value):
        """Set Function."""
        self.__parent_script = value

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                              Script (Local) Variables set Functions                                       ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_local_site_loc(self, value):
        """I am a temporary docstring."""

        if isinstance(value, hats.script_api.ScriptLoc):

            LOG.debug("   ***** ScriptLoc Object Detected For Local Site Location *****")
            self.__local_site_loc = value

        elif isinstance(value, str):

            LOG.debug("   ***** String Object Detected For Local Site Location *****")

            if value in hats.script_api.ScriptLoc.__members__:

                LOG.debug("   ***** String Is A Member Of ScriptLoc *****")
                self.__local_site_loc = hats.script_api.ScriptLoc[value]

            else:

                LOG.debug("   ***** String Not A Member Of ScriptLoc *****")
                self.__local_site_loc = hats.script_api.ScriptLoc.UNKNOWN

        else:

            LOG.debug("   ***** Unknown Object Detected For Local Site Location *****")
            self.__local_site_loc = hats.script_api.ScriptLoc.UNKNOWN

    def __set_local_ip(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__local_ip = "127.0.0.1"
        else:
            self.__local_ip = value

    def __set_local_port(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__local_port = 0
        else:
            self.__local_port = value

    def __set_local_user(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__local_user = "unknown"
        else:
            self.__local_user = value

    def __set_local_user_domain(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__local_user_domain = "unknown"
        else:
            self.__local_user_domain = value

    def __set_local_uri(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__local_uri = "unknown"
        else:
            self.__local_uri = value

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                Device Information set Functions                                           ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_remote_site_loc(self, value):
        """I am a temporary docstring."""

        if isinstance(value, hats.script_api.ScriptLoc):

            LOG.debug("   ***** ScriptLoc Object Detected For Local Site Location *****")
            self.__remote_site_loc = value

        elif isinstance(value, str):

            LOG.debug("   ***** String Object Detected For Local Site Location *****")

            if value in hats.script_api.ScriptLoc.__members__:

                LOG.debug("   ***** String Is A Member Of ScriptLoc *****")
                self.__remote_site_loc = hats.script_api.ScriptLoc[value]

            else:

                LOG.debug("   ***** String Not A Member Of ScriptLoc *****")
                self.__remote_site_loc = hats.script_api.ScriptLoc.UNKNOWN

        else:

            LOG.debug("   ***** Unknown Object Detected For Local Site Location *****")
            self.__remote_site_loc = hats.script_api.ScriptLoc.UNKNOWN

    def __set_remote_ip(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__remote_ip = "127.0.0.1"
        else:
            self.__remote_ip = value

    def __set_remote_password(self, value):
        """I am a temporary docstring."""
        self.__remote_password = value

    def __set_remote_sip_user(self, value):
        """I am a temporary docstring."""
        self.__remote_sip_user = value

    def __set_remote_user(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__remote_user = "unknown"
        else:
            self.__remote_user = value

    def __set_remote_user_domain(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__remote_user_domain = "unknown"
        else:
            self.__remote_user_domain = value

    def __set_remote_uri(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__remote_uri = "unknown"
        else:
            self.__remote_uri = value

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                Proxy Information set Functions                                            ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_local_proxy_ip(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__local_proxy_ip = "127.0.0.1"
        else:
            self.__local_proxy_ip = value

    def __set_local_proxy_password(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__local_proxy_password = "unknown"
        else:
            self.__local_proxy_password = value

    def __set_local_backup_proxy_ip(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__local_backup_proxy_ip = "127.0.0.1"
        else:
            self.__local_backup_proxy_ip = value

    def __set_local_backup_proxy_password(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__local_backup_proxy_password = "unknown"
        else:
            self.__local_backup_proxy_password = value

    def __set_remote_proxy_ip(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__remote_proxy_ip = "127.0.0.1"
        else:
            self.__remote_proxy_ip = value

    def __set_remote_proxy_password(self, value):
        """I am a temporary docstring."""

        if value == "":
            self.__remote_proxy_password = "unknown"
        else:
            self.__remote_proxy_password = value

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                 Scenario Information set Functions                                        ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                            Common Scenario set Functions                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_call_additional_header(self, value):
        """I am a temporary docstring."""
        self.__call_additional_header = value

    def __set_call_duration(self, value):
        """I am a temporary docstring."""
        self.__call_duration = value

    def __set_call_end_pause(self, value):
        """I am a temporary docstring."""
        self.__call_end_pause = value

    def __set_call_info_body(self, value):
        """I am a temporary docstring."""
        self.__call_info_body = value

    def __set_call_timing_delta(self, value):
        """I am a temporary docstring."""
        self.__call_timing_delta = value

    def __set_call_type(self, value):
        """I am a temporary docstring."""

        if isinstance(value, CallType):

            self.__call_type = value

        elif isinstance(value, str):

            if value in CallType.__members__:

                self.__call_type = CallType[value]

            else:

                self.__call_type = CallType.UNKNOWN

        else:

            self.__call_type = CallType.UNKNOWN

    def __set_scenario_file(self, value):
        """I am a temporary docstring."""

        if value != "":
            self.__scenario_file = value

    def __set_scenario_name(self, value):
        """I am a temporary docstring."""
        self.__scenario_name = value

    def __set_scenario_timeout(self, value):
        """I am a temporary docstring."""
        self.__scenario_timeout = value

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                              Common Response set Functions                                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_response_client_error_timeout(self, value):
        """I am a temporary docstring."""
        self.__response_client_error_timeout = value

    def __set_response_normal_timeout(self, value):
        """I am a temporary docstring."""
        self.__response_normal_timeout = value

    def __set_response_provisional_timeout(self, value):
        """I am a temporary docstring."""
        self.__response_provisional_timeout = value

    def __set_response_server_error_timeout(self, value):
        """I am a temporary docstring."""
        self.__response_server_error_timeout = value

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                   Allow set Functions                                          ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_allow_methods(self, value):
        """I am a temporary docstring."""
        self.__allow_methods = value

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                Initial INVITE set Functions                                    ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_initial_invite_uac_bye(self, value):
        """I am a temporary docstring."""
        self.__initial_invite_uac_bye = value

    def __set_initial_invite_uas_bye(self, value):
        """I am a temporary docstring."""
        self.__initial_invite_uas_bye = value

    def __set_initial_invite_uac_cancel(self, value):
        """I am a temporary docstring."""
        self.__initial_invite_uac_cancel = value

    def __set_initial_invite_response_code(self, value):
        """I am a temporary docstring."""
        self.__initial_invite_response_code = value

    def __set_server_initial_response_delay(self, value):
        """I am a temporary docstring."""
        self.__server_initial_response_delay = value

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                               Follow Up INVITE set Functions                                   ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_follow_up_invite_uac_bye(self, value):
        """I am a temporary docstring."""
        self.__follow_up_invite_uac_bye = value

    def __set_follow_up_invite_uas_bye(self, value):
        """I am a temporary docstring."""
        self.__follow_up_invite_uas_bye = value

    def __set_follow_up_invite_uac_cancel(self, value):
        """I am a temporary docstring."""
        self.__follow_up_invite_uac_cancel = value

    def __set_follow_up_invite_response_code(self, value):
        """I am a temporary docstring."""
        self.__follow_up_invite_response_code = value

    def __set_server_follow_up_response_delay(self, value):
        """I am a temporary docstring."""
        self.__server_follow_up_response_delay = value

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                     NOTIFY set Functions                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_notify_response_code(self, value):
        """I am a temporary docstring."""
        self.__notify_response_code = value

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                    REGISTER set Functions                                      ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_register_multi_proxies(self, value):
        """I am a temporary docstring."""
        self.__register_multi_proxies = value

    def __set_registration_expires_time(self, value):
        """I am a temporary docstring."""
        self.__registration_expires_time = value

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                   SUBSCRIBE set Functions                                      ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_subscribe_event(self, value):
        """I am a temporary docstring."""
        self.__subscribe_event = value

    def __set_subscribe_expires_time(self, value):
        """I am a temporary docstring."""
        self.__subscribe_expires_time = value

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                              SIP/SDP Media Description RTP set Functions                                  ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_media_desc_one_rtp_port(self, value):
        """I am a temporary docstring."""
        self.__media_desc_one_rtp_port = value

    def __set_media_desc_one_rtp_port_max(self, value):
        """I am a temporary docstring."""
        self.__media_desc_one_rtp_port_max = value

    def __set_media_desc_one_rtp_port_min(self, value):
        """I am a temporary docstring."""
        self.__media_desc_one_rtp_port_min = value

    def __set_media_desc_one_rtp_repeat(self, value):
        """I am a temporary docstring."""
        self.__media_desc_one_rtp_repeat = value

    def __set_media_desc_one_rtp_source(self, value):
        """I am a temporary docstring."""
        self.__media_desc_one_rtp_source = value

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                                           ║
    # ║                                               ===== Class Member Properties =====                                         ║
    # ║                                                                                                                           ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                           Properties For Call Processing                                                  ║
    # ║                                                                                                                           ║
    # ║ NOTE: Ensure that these properties are defined BELOW the get/set routines they reference                                  ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    parent_script = property(__get_parent_script, __set_parent_script,
                             doc='Object denoting an instance of ScriptAPI')

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                    Properties For Script Information (Local) Variables                                    ║
    # ║                                                                                                                           ║
    # ║ NOTE: Ensure that these properties are defined BELOW the get/set routines they reference                                  ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    local_site_loc = property(__get_local_site_loc, __set_local_site_loc,
                              doc='Enumerated value denoting the site associated with the local script')

    local_ip = property(__get_local_ip, __set_local_ip,
                        doc='String value denoting the IP Address associated with the local script')

    local_port = property(__get_local_port, __set_local_port,
                          doc='Integer value denoting the Port Number associated with the local script')

    local_uri = property(__get_local_uri, __set_local_uri,
                         doc='String value denoting the URI associated with the local script <UserName@UserDomain>')

    local_user = property(__get_local_user, __set_local_user,
                          doc='String value denoting the User Name associated with the local script')

    local_user_domain = property(__get_local_user_domain, __set_local_user_domain,
                                 doc='String value denoting the User Domain associated with the local script')

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                         Properties For Device (Remote) Variables                                          ║
    # ║                                                                                                                           ║
    # ║ NOTE: Ensure that these properties are defined BELOW the get/set routines they reference                                  ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    remote_site_loc = property(__get_remote_site_loc, __set_remote_site_loc,
                               doc='Enumerated value denoting the site associated with the remote device')

    remote_ip = property(__get_remote_ip, __set_remote_ip,
                         doc='String value denoting the IP Address associated with the remote device')

    remote_password = property(__get_remote_password, __set_remote_password,
                               doc='String value denoting the Password associated with the remote device')

    remote_sip_user = property(__get_remote_sip_user, __set_remote_sip_user,
                               doc='String value denoting the User Name associated with the remote devices SIP URI')

    remote_uri = property(__get_remote_uri,
                          doc='String value denoting the URI associated with the remote device <UserName@UserDomain>')

    remote_user = property(__get_remote_user, __set_remote_user,
                           doc='String value denoting the User Name associated with the remote device')

    remote_user_domain = property(__get_remote_user_domain, __set_remote_user_domain,
                                  doc='String value denoting the User Domain associated with the remote device')

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                             Properties For Proxy Variables                                                ║
    # ║                                                                                                                           ║
    # ║ NOTE: Ensure that these properties are defined BELOW the get/set routines they reference                                  ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    local_proxy_ip = property(__get_local_proxy_ip, __set_local_proxy_ip,
                              doc='String value denoting the IP Address associated with the proxy')

    local_proxy_password = property(__get_local_proxy_password, __set_local_proxy_password,
                                    doc='String value denoting the Password associated with the proxy')

    local_backup_proxy_ip = property(__get_local_backup_proxy_ip, __set_local_backup_proxy_ip,
                                     doc='String value denoting the IP Address associated with the backup proxy')

    local_backup_proxy_password = property(__get_local_backup_proxy_password, __set_local_backup_proxy_password,
                                           doc='String value denoting the Password associated with the backup proxy')

    remote_proxy_ip = property(__get_remote_proxy_ip, __set_remote_proxy_ip,
                               doc='String value denoting the IP Address associated with the proxy')

    remote_proxy_password = property(__get_remote_proxy_password, __set_remote_proxy_password,
                                     doc='String value denoting the Password associated with the proxy')

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                       Properties For Scenario Information Variables                                       ║
    # ║                                                                                                                           ║
    # ║ NOTE: Ensure that these properties are defined BELOW the get/set routines they reference                                  ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                               Common Scenario Properties                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    call_additional_header = property(__get_call_additional_header, __set_call_additional_header,
                                      doc='Append INVITE message header with custom arguments (dictionary as HeaderName: Value)')

    call_duration = property(__get_call_duration, __set_call_duration,
                             doc='Integer value denoting time (in ms) for SIPp to keep the call active')

    call_end_pause = property(__get_call_end_pause, __set_call_end_pause,
                              doc='Integer value denoting time (in ms) for SIPp to pause at the end of a call')

    call_info_body = property(__get_call_info_body, __set_call_info_body,
                              doc='Change INFO message SDP to custom message')

    call_timing_delta = property(__get_call_timing_delta, __set_call_timing_delta,
                                 doc='Integer value denoting the offset (in ms) to add to call handling operations')

    call_type = property(__get_call_type, __set_call_type,
                         doc='Enumerated value denoting the type of SIP Call to create (used for headers, etc)')

    scenario_file = property(__get_scenario_file, __set_scenario_file,
                             doc='String value denoting the file to use as a scenario (if blank, create a new one)')

    scenario_name = property(__get_scenario_name, __set_scenario_name,
                             doc='String value denoting the value to use for a scenario')

    scenario_timeout = property(__get_scenario_timeout, __set_scenario_timeout,
                                doc='Integer value denoting time (in ms) for SIPp to wait on an action')

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                 Common Response Properties                                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    response_client_error_timeout = property(__get_response_client_error_timeout, __set_response_client_error_timeout,
                                             doc='Integer value denoting time (in ms) for SIPp to wait for client error responses')

    response_normal_timeout = property(__get_response_normal_timeout, __set_response_normal_timeout,
                                       doc='Integer value denoting time (in ms) for SIPp to wait for normal responses')

    response_provisional_timeout = property(__get_response_provisional_timeout, __set_response_provisional_timeout,
                                            doc='Integer value denoting time (in ms) for SIPp to wait for provisional responses')

    response_server_error_timeout = property(__get_response_server_error_timeout, __set_response_server_error_timeout,
                                             doc='Integer value denoting time (in ms) for SIPp to wait for server error responses')

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                      Allow Properties                                          ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    allow_methods = property(__get_allow_methods, __set_allow_methods,
                             doc='Enumerated value denoting the SIP Methods to accept from proxy (used in Allow header)')

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                   Initial INVITE Properties                                    ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    initial_invite_uac_bye = property(__get_initial_invite_uac_bye, __set_initial_invite_uac_bye,
                                      doc='Boolean value denoting UAC end the init INVITE with a BYE. Default:False')

    initial_invite_uas_bye = property(__get_initial_invite_uas_bye, __set_initial_invite_uas_bye,
                                      doc='Boolean value denoting UAS end the init INVITE with a BYE. Default:False')

    initial_invite_uac_cancel = property(__get_initial_invite_uac_cancel, __set_initial_invite_uac_cancel,
                                         doc='Boolean value denoting UAC end the init INVITE with a CANCEL. Default:False')

    initial_invite_response_code = property(__get_initial_invite_response_code, __set_initial_invite_response_code,
                                            doc='String value denoting the SIP code to use for responses to init INVITE.')

    server_initial_response_delay = property(__get_server_initial_response_delay, __set_server_initial_response_delay,
                                             doc='Integer value (in ms) for SIPp to wait to send init server responses.')

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                  Follow Up INVITE Properties                                   ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    follow_up_invite_uac_bye = property(__get_follow_up_invite_uac_bye, __set_follow_up_invite_uac_bye,
                                        doc='Boolean value denoting UAC end a follow up INVITE with a BYE. Default:False')

    follow_up_invite_uas_bye = property(__get_follow_up_invite_uas_bye, __set_follow_up_invite_uas_bye,
                                        doc='Boolean value denoting UAS end a follow up INVITE with a BYE. Default:False')

    follow_up_invite_uac_cancel = property(__get_follow_up_invite_uac_cancel, __set_follow_up_invite_uac_cancel,
                                           doc='Boolean value denoting UAC end a follow up INVITE with a CANCEL. Default:False')

    follow_up_invite_response_code = property(__get_follow_up_invite_response_code, __set_follow_up_invite_response_code,
                                              doc='String value denoting the SIP code to use for responses to Re-INVITE requests')

    server_follow_up_response_delay = property(__get_server_follow_up_response_delay, __set_server_follow_up_response_delay,
                                               doc='Integer value (in ms) for SIPp to wait to send follow up server responses')

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                        NOTIFY Properties                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    notify_response_code = property(__get_notify_response_code, __set_notify_response_code,
                                    doc='String value denoting the SIP code to use for responses to NOTIFY requests')

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                       REGISTER Properties                                      ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    register_multi_proxies = property(__get_register_multi_proxies, __set_register_multi_proxies,
                                      doc='Boolean value denoting whether or not to register with multiple proxies Default:False')

    registration_expires_time = property(__get_registration_expires_time, __set_registration_expires_time,
                                         doc='String value denoting time (in s) before a registration will expire')

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                      SUBSCRIBE Properties                                      ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    subscribe_event = property(__get_subscribe_event, __set_subscribe_event,
                               doc='String value denoting the name of the event to subscribe with')

    subscribe_expires_time = property(__get_subscribe_expires_time, __set_subscribe_expires_time,
                                      doc='String value denoting time (in s) before a subscription will expire')

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                      Properties For SIP/SDP Media Description RTP Variables                               ║
    # ║                                                                                                                           ║
    # ║ NOTE: Ensure that these properties are defined BELOW the get/set routines they reference                                  ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    media_desc_one_rtp_port = property(__get_media_desc_one_rtp_port, __set_media_desc_one_rtp_port,
                                       doc='Integer value denoting the port number for SIPp to use for media desc one port')

    media_desc_one_rtp_port_max = property(__get_media_desc_one_rtp_port_max, __set_media_desc_one_rtp_port_max,
                                           doc='Integer value denoting the maximum port number for SIPp to use for media ports')

    media_desc_one_rtp_port_min = property(__get_media_desc_one_rtp_port_min, __set_media_desc_one_rtp_port_min,
                                           doc='Integer value denoting the minimum port number for SIPp to use for media ports')

    media_desc_one_rtp_repeat = property(__get_media_desc_one_rtp_repeat, __set_media_desc_one_rtp_repeat,
                                         doc='Integer value denoting the number of times to send the RTP audio source')

    media_desc_one_rtp_source = property(__get_media_desc_one_rtp_source, __set_media_desc_one_rtp_source,
                                         doc='String value denoting the file to use as an RTP audio source')

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     build_sip_action_command                                                                                          ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to generate the session parameters of an SDP message                                                     ║
    # ║                                                                                                                           ║
    # ║ @return String value containing the generated SDP session                                                                 ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def build_sip_action_command(self, pipeline_name, command_name):
        """Generate a SIPp action."""

        fname = 'SipAPI.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        action_command = ""
        command_args = []

        if command_name == SipPipelineActions.CHECK_POINT_CALL_ME:

            command = "checkpointCallMe"

        elif command_name == SipPipelineActions.CHECK_POINT_RINGING:

            command = "checkpointRinging"

        else:

            command = "unknown"

        if command != "unknown":

            # All SIP Action Commands Have The Same Arguments
            command_args.append(str(self.call_type.name))
            command_args.append(str(self.call_duration))
            command_args.append(self.remote_ip)
            command_args.append(self.remote_user)
            command_args.append(self.remote_password)
            command_args.append(self.local_ip)
            command_args.append(self.local_user)
            command_args.append(self.local_user_domain)

            action_command = hats.pipeline_api.HATS_PIPELINE_CONNECTOR
            action_command = action_command + " {} '{} {}!'".format(pipeline_name, command, " ".join(command_args))

        LOG.debug("%s Exiting", fname)
        return action_command

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     generate_sdp_session                                                                                              ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to generate the session parameters of an SDP message                                                     ║
    # ║                                                                                                                           ║
    # ║ @return String value containing the generated SDP session                                                                 ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def generate_sdp_session(self):
        """Function to generate the session parameters of an SDP message

        This function creates the 'common' component of an SDP message
        """

        fname = 'SipAPI.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            sdp = ""

            # Set the session level parameters of the SDP
            sdp += "v=0" + "\r\n"
            sdp += "o=" + str(self.local_user) + " "
            sdp += str(ntplib.system_to_ntp_time(time.time())).split(".")[0] + " "
            sdp += str(ntplib.system_to_ntp_time(time.time())).split(".")[0] + " "
            sdp += "IN" + " "
            sdp += "IP4" + " "
            sdp += str(self.local_ip) + "\r\n"
            sdp += "s=SIP Call" + "\r\n"
            sdp += "c=IN" + " "
            sdp += "IP4" + " "
            sdp += str(self.local_ip) + "\r\n"
            sdp += "t=0 0" + "\r\n"

            # Set the communication direction based on call type
            if self.call_type == CallType.VOICE_MON or self.call_type == CallType.IP_VOICE:

                sdp += "a=recvonly" + "\r\n"

            # elif self.getCallType() == CallType.IC_VOICE:

            #    sdp += "a=sendonly" + "\r\n"

            else:

                sdp += "a=sendrecv" + "\r\n"

            LOG.debug("   Generated SDP Session:\n%s\n", sdp)
            return sdp

        except Exception, ex:

            template = "   Error Creating SDP - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)
            return ""

        finally:

            LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     generate_sdp_session                                                                                              ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to generate the session parameters of an SDP message                                                     ║
    # ║                                                                                                                           ║
    # ║ @return String value containing the generated SDP session                                                                 ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def generate_sdp_media(self, initial_request=True):
        """I am a temporary docstring."""

        fname = 'SipAPI.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            current_media_desc = 1

            # Populate the Session Description for the SDP
            sdp = self.generate_sdp_session()

            while True:

                # Obtain a valid port for RTP
                rtp_port = -10

                # RTP Direction Flags
                rtp_dir_inactive = False
                rtp_dir_recvonly = False
                rtp_dir_sendonly = False

                # Attributes
                ptime = 0

                # Start with a list of all the vocoder(s) (ordered by priority)
                payload_types = ["0", "8", "15", "18", "101", "123"]

                # Process Media Description One
                if current_media_desc == 1:

                    # Use the appropriate codecs base on INVITE or RE-INVITE
                    if initial_request:

                        media_desc_one_codecs = self.parent_script.cmd_media_desc_one_rtp_initial_codecs

                    else:

                        media_desc_one_codecs = self.parent_script.cmd_media_desc_one_rtp_follow_up_codecs


                    # Verify that the codec list is not empty
                    LOG.debug("   ***** Media Description One Codecs: %s *****", str(media_desc_one_codecs))
                    if not media_desc_one_codecs:

                        LOG.debug("   ***** No codec supplied, using ALaw as default *****")
                        payload_types = ["8"]

                    else:

                        # Remove the vocoder(s) that are not specified
                        if not "0" in media_desc_one_codecs:

                            # Neither 0 nor 101 is in the codec list
                            LOG.debug("   ***** Removing uLaw codec *****")
                            payload_types.remove("0")

                            LOG.debug("   ***** Removing TelEvt codec *****")
                            payload_types.remove("101")

                        elif not "101" in media_desc_one_codecs:

                            LOG.debug("   ***** Removing TelEvt codec *****")
                            payload_types.remove("101")

                        else:

                            LOG.debug("   ***** Removing uLaw codec *****")
                            payload_types.remove("0")

                        if not "8" in media_desc_one_codecs:

                            # Neither 8 nor 18 is in the codec list
                            LOG.debug("   ***** Removing ALaw codec *****")
                            payload_types.remove("8")

                            LOG.debug("   ***** Removing G729 codec *****")
                            payload_types.remove("18")

                        elif not "18" in media_desc_one_codecs:

                            LOG.debug("   ***** Removing G729 codec *****")
                            payload_types.remove("18")

                        else:

                            LOG.debug("   ***** Removing ALaw codec *****")
                            payload_types.remove("8")

                        if not "15" in media_desc_one_codecs:

                            LOG.debug("   ***** Removing G728 codec *****")
                            payload_types.remove("15")

                        if not "123" in media_desc_one_codecs:

                            LOG.debug("   ***** Removing R2S codec *****")
                            payload_types.remove("123")

                    # Attributes
                    ptime = self.parent_script.cmd_media_desc_one_ptime

                    # RTP Direction
                    rtp_dir_inactive = self.parent_script.cmd_media_desc_one_rtp_dir_inactive
                    rtp_dir_recvonly = self.parent_script.cmd_media_desc_one_rtp_dir_recvonly
                    rtp_dir_sendonly = self.parent_script.cmd_media_desc_one_rtp_dir_sendonly

                    # Get a port in the desired range
                    while rtp_port < 0:
                        rtp_port = hats.exec_api.get_available_port(self.media_desc_one_rtp_port_min,
                                                                    self.media_desc_one_rtp_port_max)

                    self.media_desc_one_rtp_port = rtp_port

                # Process Media Description Two
                elif current_media_desc == 2:

                    if self.parent_script.cmd_call_type != CallType.AG:

                        # Vocoder
                        payload_types = ["101"]

                        # RTP Direction
                        rtp_dir_sendonly = True

                    else:

                        # Vocoder
                        payload_types = ["123"]

                    # Attributes
                    ptime = self.parent_script.cmd_media_desc_two_ptime

                else:

                    break

                LOG.debug("   Adding media announcement to media description")
                sdp += "m=audio" + " "
                sdp += str(rtp_port) + " "
                sdp += "RTP/AVP" + " "

                # Add all the specified vocoder(s) to the media description (ordered by priority)
                sdp += str(' '.join(payload_types)) + "\r\n"

                # Add the rtpmap attribute(s) to the media description (ordered by priority)
                # NOTE: Not an if, elif construct due to the fact that multiple vocoder(s) are allowed
                LOG.debug("   Adding rtmp attribute to media description")
                if "0" in payload_types:

                    sdp += "a=rtpmap:0 PCMU/8000" + "\r\n"

                if "8" in payload_types:

                    sdp += "a=rtpmap:8 PCMA/8000" + "\r\n"

                if "15" in payload_types:

                    sdp += "a=rtpmap:15 G728/8000" + "\r\n"

                if "18" in payload_types:

                    sdp += "a=rtpmap:18 G729/8000" + "\r\n"

                if "101" in payload_types:

                    sdp += "a=rtpmap:101 telephone-event/8000" + "\r\n"
                    sdp += "a=fmtp:101 0-11,16-17,206-207" + "\r\n"

                if "123" in payload_types:

                    sdp += "a=rtpmap:123 R2S/8000" + "\r\n"

                LOG.debug("   Adding ptime attribute to media description")
                sdp += "a=ptime:" + str(ptime) + "\r\n"

                # Add the rtp direction attribute to the media description
                # Order is intentional, if multiple parameters are entered they will be processed in this order
                LOG.debug("   Adding rtp direction attribute to media description")
                if rtp_dir_inactive:

                    sdp += "a=inactive" + "\r\n"

                elif rtp_dir_recvonly:

                    sdp += "a=recvonly" + "\r\n"

                elif rtp_dir_sendonly:

                    sdp += "a=sendonly" + "\r\n"

                else:

                    sdp += "a=sendrecv" + "\r\n"

                LOG.debug("   Adding custom attributes to media description")
                sdp += "a=maxptime:30" + "\r\n"

                # Add call type specific attributes to the media description
                if self.call_type == CallType.IC_OVR:

                    LOG.debug("   Adding IC_OVR attributes to media description")
                    sdp += "a=service:duplex" + "\r\n"

                elif self.call_type == CallType.IC_VOICE:

                    LOG.debug("   Adding IC_VOICE attributes to media description")
                    sdp += "a=singcalling" + "\r\n"

                elif self.call_type == CallType.AG:

                    LOG.debug("   Adding AG attributes to media description")
                    sdp += "a=ptt_rep:0" + "\r\n"
                    sdp += "a=type:Radio-TxRx" + "\r\n"
                    sdp += "a=R2S-KeepAlivePeriod:200" + "\r\n"
                    sdp += "a=R2S-KeepAliveMultiplier:10" + "\r\n"
                    sdp += "a=txrxmode:TxRx" + "\r\n"
                    sdp += "a=fid:119.300" + "\r\n"

                # Add second media description for TMG based calls
                if current_media_desc == 1:

                    #current_media_desc = current_media_desc + 1

                #else:

                    break

            LOG.debug("   Generated SDP:\n%s\n", sdp)
            return sdp

        except Exception, ex:

            template = "   Error Creating SDP - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)
            return ""

        finally:

            LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     invite_remote_uac                                                                                                 ║
    # ║                                                                                                                           ║
    # ║ @brief  Generate a SIPp XML scenario for a SIP INVITE REQUEST where this script is the call receiver (UAS)                ║
    # ║                                                                                                                           ║
    # ║ @param  sdp_initial - String value containing the SDP payload for the initial INVITE                                      ║
    # ║ @param  sdp_follow_up - String value containing the SDP payload for a follow up INVITE                                    ║
    # ║ @param  is_gg_call - Boolean value denoting whether or not the call is a G/G call                                         ║
    # ║                                                                                                                           ║
    # ║ @return String value containing the generated XML scenario                                                                ║
    # ║                                                                                                                           ║
    # ║ @note                                                                                                                     ║
    # ║         SIPp Attributes Common To All Commands                                                                            ║
    # ║         --------------------------------------                                                                            ║
    # ║            http://sipp.sourceforge.net/doc/reference.html#Create+your+own+XML+scenarios                                   ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def invite_remote_uac(self, sdp_initial, sdp_follow_up=None, is_gg_call=True):
        """Generate a SIPp XML scenario for a SIP INVITE REQUEST where this script is the call receiver (UAS)."""

        fname = 'SipAPI.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            # Generate the scenario file
            msg = "   Generating Scenario File: %s"
            if self.scenario_file is None:
                LOG.info(msg, "default")
                sippXML.startScenario("Receive Normal Call")
            else:
                LOG.info(msg, self.scenario_file)
                sippXML.startScenario("Receive Normal Call", self.scenario_file)

            # Generate the server header data
            hats_sip_server = "hats SipAPI/" + str(__version__)

            # Configure Call Type
            LOG.debug("   ***** Configuring Call Type *****")
            if self.parent_script.cmd_call_type is not None:
                self.call_type = self.parent_script.cmd_call_type

            # Configure Local and Remote Parameters
            LOG.debug("   ***** Configuring Local And Remote Parameters *****")
            sippXML.setLocalUser(self.local_user)
            sippXML.setLocalUserDomain(self.local_user_domain)
            sippXML.setRemoteUser(self.remote_sip_user)
            sippXML.setRemoteUserDomain(self.remote_user_domain)

            # Create the initialize section
            sippXML.addInit()

            # Initiate the remote call
            callme_command = self.build_sip_action_command(HATS_SIP_PIPE, SipPipelineActions.CHECK_POINT_CALL_ME)
            if callme_command != "":

                LOG.debug("   ***** Generating Action: %s To Force Remote To Make Call *****", callme_command)
                sippXML.addAction("exec", {"command": callme_command})

            else:

                raise Exception('Unable to generate Call Me action')

            # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
            # ║                                            Receive Initial INVITE Request                                         ║
            # ║                                                 <SIP Flow Item G1>                                                ║
            # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            LOG.info("   Generating Reception Handler For INVITE Request")

            sipp_request_options = {"crlf": sippXML.CRLF_ACTIVE,
                                    "timeout": self.scenario_timeout,
                                    "ontimeout": "endBranch"}

            sippXML.recvRequest("INVITE", sippOptions=sipp_request_options)

            LOG.debug("   ***** Generate Regular Expression To Obtain Header Data From The INVITE Request *****")

            # Obtain the from tag
            sippXML.addAction("ereg", {"regexp": "tag=[0-9A-Za-z]*?",
                                       "search_in": "hdr",
                                       "header": "From",
                                       "assign_to": "1"})

            # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
            # ║                                    Send Provisional Response to Initial INVITE Request                            ║
            # ║                                                <SIP Flow Item G2-2>                                               ║
            # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            LOG.info("   Generate Provisional Response: 180 For Initial INVITE Request")

            response_header_options = {"Contact": "[local_user]<sip:[local_user]@[local_ip]:[local_port]>",
                                       "Record-Route": "[last_Record-Route:]",
                                       "WG67-Version": "phone.01"}

            sippXML.sendResponse("180", responseHeaderOptions=response_header_options)

            if self.server_initial_response_delay > 0:

                LOG.debug("   ***** Creating A Delay In The Servers Final Response To The Initial INVITE Request *****")
                sippXML.pause(self.server_initial_response_delay)

            # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
            # ║                                                                                                                   ║
            # ║                                ===== Initial INVITE Req Can Be Cancelled Or Responded =====                       ║
            # ║                                                                                                                   ║
            # ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
            # ║                                        <SIP Flow Item Y1> or <SIP Flow Item G3>                                   ║
            # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            if self.initial_invite_uac_cancel:

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                          Receive CANCEL Request                                           ║
                    # ║                                            <SIP Flow Item Y1>                                             ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.info("   Generating Reception Handler For CANCEL Request")

                    sipp_request_options = {"crlf": sippXML.CRLF_ACTIVE,
                                            "timeout": self.scenario_timeout,
                                            "ontimeout": "endBranch"}

                    sippXML.recvRequest("CANCEL", sippOptions=sipp_request_options)

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                      Send 200 OK Response for CANCEL                                      ║
                    # ║                                             <SIP Flow Item Y2>                                            ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.debug("   Generating Normal Response: 200 For CANCEL Request")

                    sipp_response_options = {"retrans": "1000"}

                    response_header_options = {"Contact": "[local_user]<sip:[local_user]@[local_ip]:[local_port]>",
                                               "Record-Route": "[last_Record-Route]",
                                               "WG67-Version": "phone.01"}

                    sippXML.sendResponse("200",
                                         sippResponseOptions=sipp_response_options,
                                         responseHeaderOptions=response_header_options)

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                      Send 487  Response for CANCEL                                        ║
                    # ║                                             <SIP Flow Item Y3>                                            ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.debug("   Generating Request Terminated Response: 487 For CANCEL Request *****")

                    sipp_response_options = {"retrans": "1000"}

                    response_header_options = {"Contact": "[local_user]<sip:[local_user]@[local_ip]:[local_port]>",
                                               "Record-Route": "[last_Record-Route]",
                                               "WG67-Version": "phone.01"}

                    sippXML.sendResponse("487",
                                         sippResponseOptions=sipp_response_options,
                                         responseHeaderOptions=response_header_options)

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                                 Receive ACK                                               ║
                    # ║                                             <SIP Flow Item Y4>                                            ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.info("   Generating Reception Handler For ACK Request")

                    sipp_request_options = {"crlf": sippXML.CRLF_ACTIVE,
                                            "timeout": self.scenario_timeout,
                                            "ontimeout": "endBranch",
                                            "next": "endBranch"}

                    sippXML.recvRequest("ACK", sippOptions=sipp_request_options)

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                                                                                           ║
                    # ║                                         ===== Call Ends Here =====                                        ║
                    # ║                                                                                                           ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝

            # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
            # ║                                 Send Response to Initial INVITE Request (Other or 200)                            ║
            # ║                                            <SIP Flow Items G3-1 - G3-5>                                           ║
            # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            LOG.info("   Generate Final Response To Initial INVITE Request")
            if self.initial_invite_response_code != "200":

                LOG.debug("   ***** Generate Abnormal Response: %s For INVITE Request *****", self.initial_invite_response_code)

                sipp_response_options = {"retrans": "1000",
                                         "next": "endBranch"}

                response_header_options = {"WG67-Version": "phone.01",
                                           "Record-Route": "[last_Record-Route]"}

            else:

                LOG.debug("   ***** Generate Normal Response: %s For INVITE Request *****", self.initial_invite_response_code)

                sipp_response_options = {"retrans": "1000"}

                response_header_options = {"Contact": "[local_user]<sip:[local_user]@[local_ip]:[local_port]>",
                                           "Content-Type": "application/sdp",
                                           "Supported": "replaces",
                                           "WG67-Version": "phone.01",
                                           "Record-Route": "[last_Record-Route:]",
                                           "Body": sdp_initial}

            sippXML.sendResponse(self.initial_invite_response_code,
                                 sippResponseOptions=sipp_response_options,
                                 responseHeaderOptions=response_header_options)

            # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
            # ║                                     Receive ACK Request for Initial INVITE Request                                ║
            # ║                                                 <SIP Flow Item G4>                                                ║
            # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            LOG.info("   Generating Reception Handler For ACK Request From Initial INVITE Request")

            sipp_request_options = {"crlf": sippXML.CRLF_ACTIVE,
                                    "timeout": self.scenario_timeout,
                                    "ontimeout": "endBranch"}

            sippXML.recvRequest("ACK", sippOptions=sipp_request_options)

            # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
            # ║                                                                                                                   ║
            # ║     ===== Initial INVITE Req Can Have A Follow Up INVITE Req or INFO Req Or UAC BYE Req or UAS BYE Req  =====     ║
            # ║                                                                                                                   ║
            # ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
            # ║                  <SIP Flow Item S1> or <SIP Flow Item J1> or <SIP Flow Item G5> or <SIP Flow Item G7>             ║
            # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            if sdp_follow_up is not None:

                # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                # ║                                       Receive Second INVITE Request (Re-INVITE)                               ║
                # ║                                                 <SIP Flow Item S1>                                            ║
                # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                LOG.info("   Media-Negotiation Detected: Generating Reception Handler For RE-INVITE Request")

                sipp_request_options = {"crlf": sippXML.CRLF_ACTIVE,
                                        "timeout": self.scenario_timeout,
                                        "ontimeout": "endBranch"}

                sippXML.recvRequest("INVITE", sippOptions=sipp_request_options)

                LOG.debug("   ***** Generate Regular Expression To Obtain Header Data From The RE-INVITE Request *****")

                # Obtain the from tag from the re-invite
                sippXML.addAction("ereg", {"regexp": "tag=[0-9A-Za-z]*?",
                                           "search_in": "hdr",
                                           "header": "From",
                                           "assign_to": "1"})

                # Obtain the sequence number from the re-invite
                sippXML.addAction("ereg", {"regexp": ".*",
                                           "search_in": "hdr",
                                           "header": "CSeq:",
                                           "assign_to": "2"})

                # Create a placeholder for the action
                sippXML.addNop()

                # Obtain the entire via from the re-invite
                sippXML.addAction("assignstr", {"assign_to": "3",
                                                "value": "[last_Via:]"})

                # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                # ║                                     Send Provisional Response to Re-INVITE Request                            ║
                # ║                                                <SIP Flow Item S2-2>                                           ║
                # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                LOG.debug("   Generate Provisional Response: 180 For RE-INVITE Request")

                response_header_options = {"Contact": "[local_user]<sip:[local_user]@[local_ip]:[local_port]>",
                                           "Record-Route": "[last_Record-Route:]",
                                           "WG67-Version": "phone.01"}

                sippXML.sendResponse("180", responseHeaderOptions=response_header_options)

                if self.server_follow_up_response_delay > 0:

                    LOG.debug("   ***** Creating A Delay In The Servers Final Response To The Re-Invite Request *****")
                    sippXML.pause(self.server_follow_up_response_delay)

                # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                # ║                                                                                                               ║
                # ║                            ===== Follow Up INVITE Req Can Be Stopped Or Responded =====                       ║
                # ║                                                                                                               ║
                # ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
                # ║                                     <SIP Flow Item C1> or <SIP Flow Item S3>                                  ║
                # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                if self.follow_up_invite_uas_bye:

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                         UAS (this function) Sends BYE Request During Re-INVITE Processing                 ║
                    # ║                                              <SIP Flow Item C1>                                           ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.info("   UAS Sending BYE During Re-INVITE Processing: Generating BYE Request")

                    sipp_request_options = {"retrans": "5000"}

                    request_header_options = {"To": "[remote_user]<sip:[remote_user]@[remote_user_domain]:[remote_port]>;[$1]",
                                              "Request-Header-URI": "[local_user]@" + self.remote_ip + ":[remote_port]",
                                              "Route": "<sip:" + self.local_proxy_ip + ";lr>",
                                              "WG67-Version": "phone.01"}

                    sippXML.sendRequest("BYE", sipp_request_options, request_header_options)

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                     Receive 200 Response For BYE Request                                  ║
                    # ║                                              <SIP Flow Item C2>                                           ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.info("   Generating Normal Reception Handler For BYE Request, Timeout: %s",
                             str(self.response_normal_timeout))

                    sipp_response_options = {"crlf": sippXML.CRLF_ACTIVE,
                                             "optional": sippXML.NOT_OPTIONAL,
                                             "timeout": str(self.response_normal_timeout)}

                    sippXML.recvResponse("200", sippOptions=sipp_response_options)

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                          Receive CANCEL Request                                           ║
                    # ║                                            <SIP Flow Item C3>                                             ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.info("   Generating Reception Handler For CANCEL Request")

                    sipp_request_options = {"crlf": sippXML.CRLF_ACTIVE,
                                            "timeout": self.scenario_timeout,
                                            "ontimeout": "endBranch"}

                    sippXML.recvRequest("CANCEL", sippOptions=sipp_request_options)

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                      Send 200 OK Response for CANCEL                                      ║
                    # ║                                             <SIP Flow Item C4>                                            ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.info("   Generating Normal Response: 200 For CANCEL Request")

                    #sipp_response_options = {"retrans": "1000"}

                    response_header_options = {"To": "[last_To:]",
                                               "Server": hats_sip_server}

                    sippXML.sendResponse("200", responseHeaderOptions=response_header_options)

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                      Send 487  Response for CANCEL                                        ║
                    # ║                                             <SIP Flow Item C5>                                            ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.info("   Generating Request Terminated Response: 487 For CANCEL Request")

                    #sipp_response_options = {"retrans": "1000"}

                    response_header_options = {"To": "[last_To:]",
                                               "CSeq": "[$2]",
                                               "Via": "[$3]",
                                               "Server": hats_sip_server}

                    sippXML.sendResponse("487", responseHeaderOptions=response_header_options)

                    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                    # ║                                                 Receive ACK                                               ║
                    # ║                                             <SIP Flow Item C6>                                            ║
                    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                    LOG.info("   Generating Reception Handler For ACK Request")

                    sipp_request_options = {"crlf": sippXML.CRLF_ACTIVE,
                                            "timeout": self.scenario_timeout,
                                            "ontimeout": "endBranch"}

                    sippXML.recvRequest("ACK", sippOptions=sipp_request_options)

            # If this is a G/G call, the remote device will tell us when the party is over
            if is_gg_call:

                # Receive BYE Request for Initial INVITE Request
                LOG.info("   Generating Reception Handler For BYE Request")
                sippXML.recvRequest("BYE", dict(crlf=sippXML.CRLF_ACTIVE,
                                                timeout=self.scenario_timeout,
                                                ontimeout="endBranch"))

                LOG.debug("   ***** Generating Normal Response: 200 For BYE Request *****")
                sippXML.sendResponse("200", dict(retrans="1000", next="endBranch"),
                                     responseHeaderOptions={"Contact": "[local_user]<sip:[local_user]@[local_ip]:[local_port]>",
                                                            "Content-Type": "application/sdp",
                                                            "Supported": "replaces",
                                                            "WG67-Version": "phone.01",
                                                            "Record-Route": "[last_Record-Route]"})

            else:

                # Send the BYE Request
                LOG.info("   Generating BYE Request")
                sippXML.sendRequest("BYE",
                                    dict(retrans="5000"),
                                    requestHeaderOptions={"WG67-Version": "phone.01",
                                                          "To":
                                                          "[remote_user]<sip:[remote_user]@[remote_user_domain]:[remote_port]>;[$1]",
                                                          "Route": "<sip:" + self.local_proxy_ip + ";lr>"})

                # Receive Response (Process the various possible responses)
                LOG.debug("   ***** Generating Error Reception Handlers For BYE Request Responses *****")
                sippXML.recvResponse("404", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next="endBranch"))
                sippXML.recvResponse("408", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next="endBranch"))
                sippXML.recvResponse("481", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next="endBranch"))

                LOG.debug("   ***** Generating Normal Reception Handler For BYE Request *****")
                sippXML.recvResponse("200", dict(crlf=sippXML.CRLF_ACTIVE, timeout=self.scenario_timeout, ontimeout="endBranch"))

            # End Branch
            LOG.debug("   ***** Generating Branch Label endBranch *****")
            sippXML.addLabel("endBranch")

            # Generate the scenario xml from SIPp
            LOG.info("   Creating Scenario XML")
            scenario_xml = sippXML.generateLoadedScenario()

            # Define CDATA Indent
            cd_indent = "         "

            LOG.debug("   ***** Cleanup CDATA open tags *****")
            open_cdata_regex = re.compile(r".*(<!\[CDATA\[)")
            for line in fileinput.input([scenario_xml], inplace=True, backup='.bak'):

                line = open_cdata_regex.sub(r"      \1", line.rstrip())
                print(line)

            LOG.debug("   ***** Cleanup CDATA close tags *****")
            close_cdata_regex = re.compile(r".*(\]\]>)")
            for line in fileinput.input([scenario_xml], inplace=True, backup='.bak'):

                line = close_cdata_regex.sub(r"      \1\n", line.rstrip())
                print(line)

            # Store the scenario
            tmp_scenario = SippXmlScenario(call=self,
                                           remoteuser=self.local_proxy_ip,
                                           file=scenario_xml,
                                           backup=False)
            self.parent_script.executor.sipp_xml_scenarios.append(tmp_scenario)

            return scenario_xml

        except Exception, ex:

            template = "   Error Creating Single Invite Remote As UAC Scenario - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)
            return ""

        finally:

            LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     invite_remote_uas                                                                                                 ║
    # ║                                                                                                                           ║
    # ║ @brief  Generate a SIPp XML scenario for a SIP INVITE REQUEST where this script is the call sender (UAC)                  ║
    # ║                                                                                                                           ║
    # ║ @param  sdp - String value containing the SDP payload for the call                                                        ║
    # ║ @param  remote_answer - Boolean value denoting whether the remote should answer this call                                 ║
    # ║                                                                                                                           ║
    # ║ @return String value containing the generated XML scenario                                                                ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def invite_remote_uas(self, sdp, remote_answer=False):
        """Generate a SIPp XML scenario for a SIP INVITE REQUEST where this script is the call sender (UAC)."""

        fname = 'SipAPI.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            # Create the scenario file
            msg = "   Generating Scenario File: %s"
            if self.scenario_file is None:
                LOG.debug(msg, "default")
                sippXML.startScenario("Invite")
            else:
                LOG.debug(msg, self.scenario_file)
                sippXML.startScenario("Invite", self.scenario_file)

            # Configure Call Type
            LOG.debug("   Configuring Call Type")
            if self.parent_script.cmd_call_type is not None:
                self.call_type = self.parent_script.cmd_call_type

            # Configure Local and Remote Parameters
            LOG.debug("   ***** Configuring Local And Remote Parameters *****")
            sippXML.setLocalUser(self.local_user)
            sippXML.setLocalUserDomain(self.local_user_domain)
            sippXML.setRemoteUser(self.remote_sip_user)
            sippXML.setRemoteUserDomain(self.remote_user_domain)

            # Initiate the remote call
            ringing_command = self.build_sip_action_command(HATS_SIP_PIPE, SipPipelineActions.CHECK_POINT_RINGING)
            if ringing_command != "":

                LOG.debug("   ***** Generating Action: %s To Answer A Ringing Call *****", ringing_command)

            else:

                raise Exception('Unable to generate Ringing action')

            # Send Initial INVITE Request
            LOG.debug("   Generating INVITE Request")

            # Determine the correct subject header based on the call type enum
            subject_header = determine_subject_header(self.call_type)

            # Generate the SIP INVITE Message
            request_header_options = {"Subject": subject_header,
                                      "Priority": "normal",
                                      "Contact": "[local_user]<sip:[local_user]@[local_ip]:[local_port]>",
                                      "Content-Type": "application/sdp",
                                      "Supported": "replaces",
                                      "Allow": self.allow_methods,
                                      "Allow-Events": "dialog",
                                      "WG67-Version": "phone.01",
                                      "User-Agent": "hats sipAPI/" + __version__,
                                      "Body": sdp}

            # Depending on call type, add additional headers
            if self.call_type == CallType.VOICE_MON or self.call_type == CallType.IC_CHIME:
                request_header_options.update({"Accept": "application/sdp, message/sipfrag/",
                                               "P-ResourceState": "Unlocked;maintPos=0"})

            # ----- F1 -> Send out the INVITE -----
            sippXML.sendRequest("INVITE", dict(retrans="5000", start_txn="Invite"),
                                request_header_options.items() + self.call_additional_header.items())

            # ===== Process the various possible provisional responses =====
            LOG.debug("   Generating Provisional Reception Handlers For INVITE Request, Timeout: %s",
                      str(self.response_provisional_timeout))

            # ----- F2-1 -> Usually sent by the proxy -----
            sippXML.recvResponse("100", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_provisional_timeout)))

            # ----- F2-2 -> Usually sent by the remote device (one of the following) -----
            sippXML.recvResponse("180", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_provisional_timeout),
                                             ontimeout="provisional-responses", next="provisional-responses"))

            sippXML.addAction("exec", {"command": ringing_command})

            sippXML.recvResponse("183", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_provisional_timeout),
                                             ontimeout="provisional-responses", next="provisional-responses"))

            sippXML.addAction("exec", {"command": ringing_command})

            LOG.debug("   Generating Branch Label: provisional-responses")
            sippXML.addLabel("provisional-responses")

            # ===== Process the various possible error responses =====
            LOG.debug("   Generating Client Error Reception Handlers For INVITE Request, Timeout: %s",
                      str(self.response_client_error_timeout))

            # ----- F3-3 -> 4xx - Client Failure Responses (one of the following) -----
            sippXML.recvResponse("403", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_client_error_timeout),
                                             ontimeout="init-responses", next="error"))
            sippXML.recvResponse("404", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_client_error_timeout),
                                             ontimeout="init-responses", next="error"))
            sippXML.recvResponse("408", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_client_error_timeout),
                                             ontimeout="init-responses", next="done"))
            sippXML.recvResponse("415", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_client_error_timeout),
                                             ontimeout="init-responses", next="error"))
            sippXML.recvResponse("480", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_client_error_timeout),
                                             ontimeout="init-responses", next="error"))
            sippXML.recvResponse("481", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_client_error_timeout),
                                             ontimeout="init-responses", next="error"))
            sippXML.recvResponse("486", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_client_error_timeout),
                                             ontimeout="init-responses", next="error"))

            # ----- F3-5 -> 5xx - Server Failure Responses (one of the following) -----
            LOG.debug("   Generating Server Error Reception Handlers For INVITE Request, Timeout: %s",
                      str(self.response_server_error_timeout))
            sippXML.recvResponse("500", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_server_error_timeout),
                                             ontimeout="init-responses", next="error"))
            sippXML.recvResponse("503", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_server_error_timeout),
                                             ontimeout="init-responses", next="error"))

            LOG.debug("   Generating Branch Label: init-responses")
            sippXML.addLabel("init-responses")

            # ===== Process the final response =====
            LOG.debug("   Generating Normal Reception Handler For INVITE Request, Timeout: %s",
                      str(self.response_normal_timeout))

            # ----- F3-1 -> INVITE was received and answered -----
            sippXML.recvResponse("200", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.NOT_OPTIONAL,
                                             response_txn="Invite",
                                             timeout=str(self.response_normal_timeout),
                                             ontimeout="end"))

            # ===== Send RTP data =====
            if self.media_desc_one_rtp_source is not None:
                sippXML.addAction("exec", dict(rtp_stream=self.media_desc_one_rtp_source +
                                               "," + str(self.media_desc_one_rtp_repeat) +
                                               "," + str(self.parent_script.cmd_media_desc_one_rtp_initial_codecs)))

            # ===== Acknowledge the final response =====
            LOG.debug("   Generating ACK Request (For Provisional And Normal Responses)")

            # ----- F4 -> Send the ACK Request -----
            sippXML.sendRequest("ACK", dict(ack_txn="Invite"),
                                requestHeaderOptions={"Route": "<sip:" + self.remote_ip + ";lr>"})

            # If the call type is override, send INFO message
            if self.call_type == CallType.IC_OVR:

                # Generate the remote sipURI information
                remote_sip_uri = self.remote_user + "@" + self.remote_ip + ":5060"

                # Generate the message based on the INFO Body
                LOG.debug("   Generate INFO message")
                if self.call_info_body == " ":
                    sippXML.sendRequest("INFO", dict(retrans="5000"),
                                        requestHeaderOptions={"WG67-Version": "phone.01",
                                                              "Request-Header-URI": "sip:" + remote_sip_uri,
                                                              "Route": "<sip:" + self.local_proxy_ip + ";lr>",
                                                              "Body": "a=sid:" + self.remote_uri})
                else:
                    sippXML.sendRequest("INFO", dict(retrans="5000"),
                                        requestHeaderOptions={"WG67-Version": "phone.01",
                                                              "Request-Header-URI": "sip:" + remote_sip_uri,
                                                              "Route": "<sip:" + self.local_proxy_ip + ";lr>",
                                                              "Body": self.call_info_body})

                # ===== Process the various possible error responses =====
                LOG.debug("   Generating Client Error Reception Handlers For INFO Request, Timeout: %s",
                          str(self.response_client_error_timeout))

                # ----- I2-2 -> 4xx - Client Failure Responses (one of the following) -----
                sippXML.recvResponse("404", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next="INFOfail"))
                sippXML.recvResponse("408", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next="INFOfail"))
                sippXML.recvResponse("481", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next="INFOfail"))

                # ===== Process the final response =====
                LOG.debug("   Generating Normal Reception Handler For INFO Request, Timeout: %s",
                          str(self.response_normal_timeout))

                # ----- I2-1 -> INFO was received and answered -----
                sippXML.recvResponse("200", dict(crlf=sippXML.CRLF_ACTIVE,
                                                 timeout=self.scenario_timeout, ontimeout="INFOfail"))

                # ----- I3-3 -> Send the ACK Request -----
                LOG.debug("   Generating ACK Request (For Normal Responses)")
                sippXML.sendRequest("ACK", dict(ack_txn="Invite", next="done"),
                                    requestHeaderOptions={"Route": "<sip:" + self.remote_ip + ";lr>"})

                sippXML.addLabel("INFOfail")

            LOG.debug("   Generating Scenario Pause")
            sippXML.pause(self.call_duration)

            # If we got the 200 OK, we can opt to end the call with a BYE from the UAC or wait for the UAS to send a BYE
            if self.initial_invite_uac_bye:

                # Generate the SIP BYE Message
                request_header_options = {"To": "[remote_user]<sip:[remote_user]@[remote_user_domain]:[remote_port]>",
                                          "Route": "<sip:" + self.local_proxy_ip + ";lr>",
                                          "WG67-Version": "phone.01"}

                # ----- F5 -> Send the BYE Request -----
                LOG.debug("   Generating BYE Request")
                sippXML.sendRequest("BYE", dict(retrans="5000"), request_header_options)

                # ===== Process the various possible error responses =====

                # ----- F6-2 -> 4xx - Client Failure Responses (one of the following) -----
                LOG.debug("   Generating Client Error Reception Handlers For BYE Request, Timeout: %s",
                          str(self.response_client_error_timeout))
                sippXML.recvResponse("404", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                                 timeout=str(self.response_client_error_timeout),
                                                 ontimeout="end-responses", next="error"))
                sippXML.recvResponse("408", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                                 timeout=str(self.response_client_error_timeout),
                                                 ontimeout="end-responses", next="error"))
                sippXML.recvResponse("481", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                                 timeout=str(self.response_client_error_timeout),
                                                 ontimeout="end-responses", next="error"))

                LOG.debug("   Generating Branch Label: end-responses")
                sippXML.addLabel("end-responses")

                # ===== Process the final response =====

                # ----- F6-1 -> BYE was received and answered -----
                LOG.debug("   Generating Normal Reception Handler For BYE Request, Timeout: %s",
                          str(self.response_normal_timeout))
                sippXML.recvResponse("200", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.NOT_OPTIONAL,
                                                 timeout=str(self.response_normal_timeout),
                                                 ontimeout="end"))

                # ----- F6-3 -> Send the ACK Request -----
                LOG.debug("   Generating ACK Request (For Normal Responses)")
                sippXML.sendRequest("ACK", dict(ack_txn="Invite", next="done"),
                                    requestHeaderOptions={"Route": "<sip:" + self.remote_ip + ";lr>"})

            else:

                LOG.debug("   Generating Scenario Pause")
                sippXML.pause(self.call_duration)

                # ----- F7 -> Receive call end request -----
                LOG.debug("   Generating BYE Reception Handler")
                sippXML.recvRequest("BYE", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.NOT_OPTIONAL,
                                                timeout=str(self.scenario_timeout),
                                                ontimeout="done"))

                # ----- F8 -> Send final response -----
                LOG.debug("   Generating Normal Response: 200 For BYE Request")
                sippXML.sendResponse("200", dict(retrans="1000", next="done"),
                                     responseHeaderOptions={"Contact": "[local_user]<sip:[local_user]@[local_ip]:[local_port]>",
                                                            "Content-Type": "application/sdp",
                                                            "Supported": "replaces",
                                                            "WG67-Version": "phone.01",
                                                            "Record-Route": "[last_Record-Route]"})

            # End Branch
            LOG.debug("   Generating Branch Label: end")
            sippXML.addLabel("end")

            # Cancel the call before the final response is received
            if self.initial_invite_uac_cancel:

                LOG.debug("   Generating Scenario Pause")
                sippXML.pause(self.call_duration)

                # ----- X1 -> Send the CANCEL Request -----
                # - Mismatch in the sequence number will cause a 415 message to return
                # - Mismatch in the branch of the Via will cause a 481 message to return
                LOG.debug("   Generating CANCEL Request")
                sippXML.sendRequest("CANCEL", dict(retrans="10"),
                                    requestHeaderOptions={"To": self.remote_user + " <sip:" + self.remote_uri + ":[remote_port]>"})

                # ===== Process the various possible error responses =====
                LOG.debug("   Generating Error Reception Handlers For CANCEL Request Responses")

                # ----- X3 -> 4xx - Client Failure Responses (one of the following) ----
                sippXML.recvResponse("408", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                                 timeout=str(self.response_client_error_timeout),
                                                 ontimeout="end-responses", next="done"))
                sippXML.recvResponse("415", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                                 timeout=str(self.response_client_error_timeout),
                                                 ontimeout="end-responses", next="done"))
                sippXML.recvResponse("481", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                                 timeout=str(self.response_client_error_timeout),
                                                 ontimeout="end-responses", next="done"))

                LOG.debug("   Generating Branch Label: end-responses")
                sippXML.addLabel("end-responses")

                # ===== Process the final response =====
                LOG.debug("   Generating Normal Reception Handler For CANCEL Request")

                # ----- X2 ->  -----
                sippXML.recvResponse("200", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                                 timeout=str(self.scenario_timeout)))

                # Process the response
                sippXML.recvResponse("487", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.NOT_OPTIONAL,
                                                 response_txn="Invite",
                                                 timeout=str(self.scenario_timeout),
                                                 ontimeout="done", next="error"))

            # Error Branch
            LOG.debug("   Generating Branch Label: error")
            sippXML.addLabel("error")

            # Send the ACK Request for Errors
            LOG.debug("   Generating ACK Request (For Error Responses)")
            sippXML.setFlag(sippXML.SUBTRACT_ACK_SEQUENCE, True)
            sippXML.sendRequest("ACK",
                                requestHeaderOptions={"Route": "<sip:" + self.remote_ip + ";lr>"})
            sippXML.setFlag(sippXML.SUBTRACT_ACK_SEQUENCE, False)

            # End Branch
            LOG.debug("   Generating Branch Label: done")
            sippXML.addLabel("done")

            LOG.debug("   Generating End Of Scenario Pause")
            sippXML.pause(self.call_end_pause)

            # Generate the scenario xml from SIPp
            LOG.debug("   Creating Scenario XML")
            scenario_xml = sippXML.generateLoadedScenario()

            # Store the scenario
            tmp_scenario = SippXmlScenario(call=self,
                                           remoteuser=self.local_proxy_ip,
                                           file=scenario_xml,
                                           backup=False)
            self.parent_script.executor.sipp_xml_scenarios.append(tmp_scenario)

            return scenario_xml

        except Exception, ex:

            template = "   Error Creating Single Invite Remote As UAS Scenario - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)
            return ""

        finally:

            LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     register                                                                                                          ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to generate SIPp XML scenario for a Register. Automatically adjusts for Digest Authentication            ║
    # ║                                                                                                                           ║
    # ║ @param  script - Instance of scriptAPI                                                                                    ║
    # ║ @param  scenarioRun - Boolean for running the scenario after creation                                                     ║
    # ║                       Defaults to True                                                                                    ║
    # ║                                                                                                                           ║
    # ║ @return String value containing the generated XML scenario                                                                ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def register(self, scenario_run=True):
        """Function to generate SIPp XML scenario for a Register. Automatically adjusts for Digest Authentication.

        This function demonstrates a REGISTER behavior as defined in RFC3261.
        """
        fname = 'SipAPI.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:
            # Generate the scenario file
            msg = "   ===== Generating Scenario File: %s ====="
            if self.scenario_file is None:
                LOG.debug(msg, "default")
                sippXML.startScenario("Register")
            else:
                LOG.debug(msg, self.scenario_file)
                sippXML.startScenario("Register", self.scenario_file)

            # Configure Local Parameters
            LOG.debug("   Configuring Local Parameters")
            sippXML.setLocalUser(self.local_user)
            sippXML.setLocalUserDomain(self.local_user_domain)

            # Generate the SIP REGISTER Request Message
            LOG.debug("   Generating REGISTER Request For User: %s", self.local_uri)
            sippXML.sendRequest("REGISTER", dict(retrans="5000", next="responses"),
                                requestHeaderOptions={"Expires": self.registration_expires_time,
                                                      "Contact": "<sip:[local_user]@[local_ip]:[local_port]>;q=0.5",
                                                      "Allow": self.allow_methods})

            LOG.debug("   Generating Branch Label: secondreg")
            sippXML.addLabel("secondreg")

            # Generate the follow-up SIP REGISTER Request Message (with nonce)
            sippXML.sendRequest("REGISTER", dict(retrans="5000"),
                                requestHeaderOptions={"[authentication username=[local_user] password=password]": "",
                                                      "Expires": self.registration_expires_time,
                                                      "Contact": "<sip:[local_user]@[local_ip]:[local_port]>;q=0.5",
                                                      "Allow": self.allow_methods})

            LOG.debug("   Generating Branch Label: responses")
            sippXML.addLabel("responses")

            # 4xx - Client Failure Responses
            LOG.debug("   Generating Client Error Reception Handlers For REGISTER Request, Timeout: %s",
                      str(self.response_client_error_timeout))
            sippXML.recvResponse("400", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             next="end"))
            sippXML.recvResponse("401", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL,
                                             next="secondreg",
                                             auth="true"))

            # REGISTER was received and accepted
            LOG.debug("   Generating Normal Reception Handler For REGISTER Request, Timeout: %s",
                      str(self.response_normal_timeout))
            sippXML.recvResponse("200", dict(crlf=sippXML.CRLF_ACTIVE,
                                             timeout=str(self.response_normal_timeout)))

            LOG.debug("   Generating Branch Label: end")
            sippXML.addLabel("end")

            # Generate the scenario xml from SIPp
            LOG.debug("   Creating Scenario XML")
            scenario_xml = sippXML.generateLoadedScenario()

            # Store the scenario(s)
            tmp_scenario = SippXmlScenario(call=self,
                                           remoteuser=self.local_proxy_ip,
                                           file=scenario_xml,
                                           backup=False)
            self.parent_script.executor.sipp_xml_scenarios.append(tmp_scenario)

            if self.register_multi_proxies:
                tmp_scenario = SippXmlScenario(call=self,
                                               remoteuser=self.local_backup_proxy_ip,
                                               file=scenario_xml,
                                               backup=True)
                self.parent_script.executor.sipp_xml_scenarios.append(tmp_scenario)

            # Execute the scenario(s) (if required)
            if scenario_run:

                # Execute the scenario
                self.parent_script.executor.execute_xml_scenarios()

            return scenario_xml

        except Exception, ex:

            template = "   Error Creating Register Scenario - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)
            return ""

        finally:

            LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     subscribe                                                                                                         ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to generate SIPp XML scenario for a SUBSCRIBE                                                            ║
    # ║                                                                                                                           ║
    # ║ @param  script - Instance of scriptAPI                                                                                    ║
    # ║ @param  tmgInternal - Boolean for adding VCS21 internal protocol flag to message (Used for TMG communication              ║
    # ║                       Defaults to False                                                                                   ║
    # ║ @param  scenarioRun - Boolean for running the scenario after creation                                                     ║
    # ║                       Defaults to True                                                                                    ║
    # ║                                                                                                                           ║
    # ║ @return String value containing the generated XML scenario                                                                ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def subscribe(self, tmg_internal=False, scenario_run=True):
        """Function to generate SIPp XML scenario for a SUBSCRIBE.

        This function demonstrates a SUBSCRIBE behavior as defined in RFC3265/RFC6665.
        """
        fname = 'SipAPI.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            LOG.debug("   Generating Scenario File")
            if self.scenario_file is None:
                sippXML.startScenario("Subscribe")
            else:
                sippXML.startScenario("Subscribe", self.scenario_file)

            # Configure Local and Remote Parameters
            LOG.debug("   Configuring Local And Remote Parameters")
            sippXML.setLocalUser(self.local_user)
            sippXML.setLocalUserDomain(self.local_user_domain)
            sippXML.setRemoteUser(self.remote_user)
            sippXML.setRemoteUserDomain(self.remote_user_domain)

            # Generate the SIP SUBSCRIBE Request Message
            LOG.debug("   Generating SUBSCRIBE Request For User: %s   To: %s", self.local_uri, self.remote_uri)

            if tmg_internal is True:
                sippXML.sendRequest("SUBSCRIBE",
                                    requestHeaderOptions={"Expires": self.subscribe_expires_time,
                                                          "Event": self.subscribe_event,
                                                          "WG67-Version": "phone.01",
                                                          "P-VCS21": "level;value=1",
                                                          "Contact": "<sip:[local_user]@[local_ip]:[local_port]>;q=0.5"})
            else:

                sippXML.sendRequest("SUBSCRIBE",
                                    requestHeaderOptions={"Expires": self.subscribe_expires_time,
                                                          "Event": self.subscribe_event,
                                                          "WG67-Version": "phone.01",
                                                          "Contact": "<sip:[local_user]@[local_ip]:[local_port]>;q=0.5"})

            # Process the various possible responses
            LOG.debug("   Generating Error Reception Handlers For SUBSCRIBE Request Responses")

            # 4xx - Client Failure Responses
            sippXML.recvResponse("400", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next=1))
            sippXML.recvResponse("404", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next=1))
            sippXML.recvResponse("477", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next=1))
            sippXML.recvResponse("487", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next=1))
            sippXML.recvResponse("489", dict(crlf=sippXML.CRLF_ACTIVE, optional=sippXML.OPTIONAL, next=1))

            LOG.debug("   Generating Normal Reception Handler For SUBSCRIBE Request Response")
            sippXML.recvResponse("200", dict(crlf=sippXML.CRLF_ACTIVE, timeout=self.scenario_timeout))

            # Receive NOTIFY Request
            LOG.debug("   Generating Reception Handler For Initial NOTIFY Request")
            sippXML.recvRequest("NOTIFY", dict(crlf=sippXML.CRLF_ACTIVE, timeout=self.scenario_timeout, ontimeout=1))

            # Send Response to NOTIFY Request (Other or 200)
            LOG.debug("   Generate Response To Initial NOTIFY Request")
            if self.notify_response_code != "200":
                LOG.debug("      Generate Abnormal Response: %s For NOTIFY Request", self.notify_response_code)
                sippXML.sendResponse(self.notify_response_code,
                                     dict(responseHeaderOptions={"WG67-Version": "phone.01",
                                                                 "Record-Route": "[last_Record-Route:]",
                                                                 "To": "[last_To:]"}))
            else:
                LOG.debug("      Generate Normal Response: %s For NOTIFY Request", self.notify_response_code)
                sippXML.sendResponse(self.notify_response_code,
                                     dict(responseHeaderOptions={"WG67-Version": "phone.01",
                                                                 "Record-Route": "[last_Record-Route:]",
                                                                 "To": "[last_To:]"}))

            LOG.debug("   Generating Branch Label 2")
            sippXML.addLabel(2)

            # Receive NOTIFY Request
            LOG.debug("   Generating Reception Handler For Successive NOTIFY Request")
            sippXML.recvRequest("NOTIFY", dict(crlf=sippXML.CRLF_ACTIVE, timeout=self.scenario_timeout, ontimeout=1))

            # Send Response to NOTIFY Request (Other or 200)
            LOG.debug("   Generate Response To Successive NOTIFY Request")
            if self.notify_response_code != "200":
                LOG.debug("      Generate Abnormal Response: %s For NOTIFY Request", self.notify_response_code)
                sippXML.sendResponse(self.notify_response_code,
                                     dict(responseHeaderOptions={"WG67-Version": "phone.01",
                                                                 "Record-Route": "[last_Record-Route:]",
                                                                 "To": "[last_To:]"}))
            else:
                LOG.debug("      Generate Normal Response: %s For NOTIFY Request", self.notify_response_code)
                sippXML.sendResponse(self.notify_response_code,
                                     dict(responseHeaderOptions={"WG67-Version": "phone.01",
                                                                 "Record-Route": "[last_Record-Route:]",
                                                                 "To": "[last_To:]"}))

            LOG.debug("   Generating Branch Label 1")
            sippXML.addLabel(1)

            LOG.debug("   Generating End Of Scenario Pause")
            sippXML.pause(self.call_end_pause)

            # Generate the scenario xml from SIPp
            LOG.debug("   Creating Scenario XML")
            subscribe_xml = sippXML.generateLoadedScenario()

            # Store the scenario
            tmp_scenario = SippXmlScenario(call=self,
                                           remoteuser=self.local_proxy_ip,
                                           file=subscribe_xml,
                                           backup=False)
            self.parent_script.executor.sipp_xml_scenarios.append(tmp_scenario)

            # Execute the scenario (if required)
            if scenario_run:

                # Execute the scenario
                self.parent_script.executor.execute_xml_scenarios(self)

            return subscribe_xml

        except Exception, ex:

            template = "   Error Creating Subscribe Scenario - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)
            return ""

        finally:

            LOG.debug("%s Exiting", fname)
