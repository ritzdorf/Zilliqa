#!/usr/bin/env python
# Copyright (c) 2018 Zilliqa
# This source code is being disclosed to you solely for the purpose of your
# participation in testing Zilliqa. You may view, compile and run the code for
# that purpose and pursuant to the protocols and algorithms that are programmed
# into, and intended by, the code. You may not do anything else with the code
# without express permission from Zilliqa Research Pte. Ltd., including
# modifying or publishing the code (or any part of it), and developing or
# forming another public or private blockchain network. This source code is
# provided 'as is' and no warranties are given as to title or non-infringement,
# merchantability or fitness for purpose and, to the extent permitted by law,
# all liability for your use of the code is disclaimed. Some programs in this
# code are governed by the GNU General Public License v3.0 (available at
# https://www.gnu.org/licenses/gpl-3.0.en.html) ('GPLv3'). The programs that
# are governed by GPLv3.0 are those programs that are located in the folders
# src/depends and tests/depends and which include a reference to GPLv3 in their
# program files.

import subprocess
import os
import sys
import shutil
import stat
import time 

from subprocess import Popen, PIPE

NODE_LISTEN_PORT = 6001
LOCAL_RUN_FOLDER = './dsguard_rejoin_local_run/'

def print_usage():
	print ("Testing multiple Zilliqa nodes in local machine\n"
		"===============================================\n"
		"Usage:\n\tpython " + sys.argv[0] + " [command] [command parameters]\n"
		"Available commands:\n"
		"\tTest Execution:\n"
		"\t\tsetup [num-nodes]           - Set up the nodes\n"
		"\t\tstart                       - Start node processes\n")

def main():
	numargs = len(sys.argv)
	if (numargs < 2):
		print_usage()
	else:
		command = sys.argv[1]
		if (command == 'setup'):
			print_usage() if (numargs != 3) else run_setup(numnodes=int(sys.argv[2]), printnodes=True)
		elif (command == 'start'):
			print_usage() if (numargs != 2) else run_start()
		else:
			print_usage()

# ================
# Helper Functions
# ================

def get_immediate_subdirectories(a_dir):
	subdirs = [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]
	subdirs.sort()
	return subdirs

# ========================
# Test Execution Functions
# ========================

def run_setup(numnodes, printnodes):
	if (os.path.exists(LOCAL_RUN_FOLDER)):
		shutil.rmtree(LOCAL_RUN_FOLDER)
	os.makedirs(LOCAL_RUN_FOLDER)
	for x in range(0, numnodes):
		testsubdir = LOCAL_RUN_FOLDER + 'node_' + str(x+1).zfill(4)
		os.makedirs(testsubdir)
		shutil.copyfile('./tests/Zilliqa/zilliqa', testsubdir + '/zilliqa_ds_guard_rejoin')

		st = os.stat(testsubdir + '/zilliqa_ds_guard_rejoin')
		os.chmod(testsubdir + '/zilliqa_ds_guard_rejoin', st.st_mode | stat.S_IEXEC)

	if printnodes:
		testfolders_list = get_immediate_subdirectories(LOCAL_RUN_FOLDER)
		count = len(testfolders_list)
		for x in range(0, count):
			print '[Node ' + str(x + 1).ljust(3) + '] [Port ' + str(NODE_LISTEN_PORT + x) + '] ' + LOCAL_RUN_FOLDER + testfolders_list[x]

def run_start():
	testfolders_list = get_immediate_subdirectories(LOCAL_RUN_FOLDER)
	count = len(testfolders_list)
	# keypairs = []

	# Generate keypairs (sort by public key)
	# for x in range(0, count):
	# 	process = Popen(["./tests/Zilliqa/genkeypair"], stdout=PIPE)
	# 	(output, err) = process.communicate()
	# 	exit_code = process.wait()
	# 	keypairs.append(output.strip())
	# keypairs.sort()

	# Store sorted keys list in text file
	# keys_file = open(LOCAL_RUN_FOLDER + 'keys.txt', "w")
	for x in range(0, count):
		# keys_file.write(keypairs[x] + '\n')
		shutil.copyfile('dsnodes.xml', LOCAL_RUN_FOLDER + testfolders_list[x] + '/dsnodes.xml')
		shutil.copyfile('constants_local.xml', LOCAL_RUN_FOLDER + testfolders_list[x] + '/constants.xml')
	# keys_file.close()

	# This keys are non critical and are only used for testing purposes
	keypairs = ["02028CC4DEC0A756B42BD54905237B4E22FCC69D88CFEAA3797AEECF01D6A69E85 55009317F8B1FC7889EDF83742F684FB700EE8F970F7EDB8BDD6286A0F0A4CF1",
					"021D99F2E5ACBA39ED5ACC5DCA5EE2ADDE780FFD998E1DBF440FE364C3BE360A7B 50C26000FCC08867FC3B9C03385015179E4B63282CB356014233BB1877FCDBDD",
					"025C8ACD69AE4075D3F02CE07641329CEFAF6C1B24BE64187D2ECDBDD55CF934A2 67E57D32E7EF421B704C23B05A7600A56808F2910FC2944CD7C7F87684CF0F49",
					"025EA8FFF868B64D5722F16FB07FB93CBFF38C5381F975CA5D0A728AEA19DBC6BC BE0CE7A97F90D433D58C873A9334819FDBF2646E08F61B470ACF996C082F0BB7",
					"0268B2A0B5FFE2ADE7A38DF9A878281A8BFFA4F8EE18A20EE53F5ABA3BDDC6BF00 A351988F0776D25CE203EC21BDBAF4402E98A2A9A724C28A8E4FEC81F030AF55",
					"027612A13BFA87AB22C0B3166B14873C7BEB77F0A27970BB0D1788EAA5F1BB885A 9C0A58E554511887E39E1E9BC25874B921A13FAFBB7DD4D57C8EBE6D72938C7D",
					"028ED45F00C33680BFDBBADD8DDC98627BF18E7B49E83420C00DE9C9752FE8F33D 33DB54623E8AFDFE735E1D73C62F68C924811DD5CD3300FE5203B580E330A373",
					"02B006BEAAFABFB738822EB4DFE3C0872A426173FF4C154D083A9C0EC5EB78A0C6 51D0976A2A9E72198D78BF229E8AB34DD9AE9E093CB1B71B4853C6839130CB6B",
					"02B5D018B064A26998AD4553BD5D394E898043A9C5A4E414C9EA71F1B26E1CEF3F 13A8B01932B072D1225BDD550C5D4048F664D3AE2476F24FD1EFF123573563F5",
					"02C28CDFC2CE6CE00DC38F5DBE565034BE50D382CB63FC260DA91E6828F806AAB6 C106836B85D5498112A13081A60326988012F6B0ED39480E3AB5683C69E04CB7",
					"02E1626300DA30EFC798DEB27ED546BB2B4D1D8771E0907B1DAD3A0AD3BE1381CD 3016CB647ABBD35B85939FC716155777DCC41AEB54D5498A0A99BCE74A2BF119",
					"02F650040BC0F3158B5D1A870EFC0ABE84FF02A4021A222FC49F9AD070ACFA2DA7 797FD9258980F9669A86E006A679815D15BD899B607454C3EDF284846F13E7E7",
					"030DFD4A0CFD68016DF6EFC4A6BF0B67BA42ABEAF8D9AD65C25E97B9DA90CA4DB1 50481C07CA036990945EBE3A0B7D71FFCCF27CFF4B1DA03B1C8FB3660DA89552",
					"03129EAEF8A136355FB1485941A593B4BEC4DFC5504D1114138A6D92332005DC59 CC3927D2C18849E6CFA3EE6D9322718961D2F035A1359AD1F37EEF527B5FBB15",
					"037D49C420B04B9862BC1F0660544FF27F1D81EA0E5E7C161F1647FBF239F8780E EB4D499149C3582AD84CCB28E697EB0BCAF331CD7CBE43D5672C21BB9C17A477",
					"03A6738E9081002097DDC71E3B72F9BBA2C0482034B8E80512D1B2DA5FFFFCBF8E 1430F36192D10C8ABCD9A22B036788C13F17830E807FEC7073B5E14E4B171265",
					"03C58CD6B4C6A0E4FEC1D989D3218B67AFC82149039E174074C5FDFE58CB427028 38EB4FB242BCD8D4BBD9114307F9B7F1F90D8DB7DE0AEC356691BEC98642C062",
					"03D616566DE986ADAC0E51BAF8147155993D56CCE4834607CFDDF832C3CAFD00F7 B459705C716E12044AB8263F812A9E9153269DD1449FA3B40EAA489F844BF839",
					"03E4DA9E02B0830C98E99737FE63B34D068D086184583449C583A68F4DBA79BE64 7541CE8176B260B4A6D28578D2433D17A7948F3810E464C5288E86E7DCDC71AE",
					"03FB81D476B3CF161AFD1AE0B861ECC907111AB891DF82028DD3D3085E2460A574 224B31816F0B529F21B14D9F04C42E7F277A024758A57BB6E1B3DEBF39A38E72"]


	# Launch node zilliqa process
	keypair = keypairs[1].split(" ")
	os.system('cd ' + LOCAL_RUN_FOLDER + testfolders_list[x] + '; echo \"' + keypair[0] + ' ' + keypair[1] + '\" > mykey.txt' + '; ulimit -n 65535; ulimit -Sc unlimited; ulimit -Hc unlimited; ./zilliqa_ds_guard_rejoin ' + keypair[1] + ' ' + keypair[0] + ' ' + '127.0.0.1' + ' '  + str(7001) + ' 0 7 0 > ./error_log_zilliqa 2>&1 &')

if __name__ == "__main__":
	main()