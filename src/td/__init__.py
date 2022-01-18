from __future__ import annotations
from .shared import *


# class TDesktop(TDesktop):

#     def ImportTelethonAccount(self, telethonClient : telethon.TelegramClient) -> bool:

#         excpt.Expects(self.accountsCount < TDesktop.kMaxAccounts,
#         exception=excpt.MaxAccountLimit("You can't have more than 3 accounts in one TDesktop clent.\n"\
#                                         "Please create another instance of TDesktop or use Account.FromTelethon() to create an Account() independently"))
        
        
        
#         # newAccount.serializeMtpAuthorization()
#         # newAccount.prepareToStart(self.__localKey)
#         # if not newAccount.isLoaded():
#         #     return False 
        
#         # self.accounts.append(newAccount)
#         return True

# class TDesktop(TDesktop):
#     async def ToNewTelethonSession(self, session_name : str, customAPI : API = None) -> TelegramClient:
        
#         resolve_file_name = session_name
#         if resolve_file_name[-8:] != ".session": resolve_file_name += ".session"

#         if os.path.exists(resolve_file_name):
#             os.remove(resolve_file_name)

#         if customAPI != None:
#             newClient = TelegramClient(session_name, customAPI.api_id, customAPI.api_hash, device_model=customAPI.pid) # pass hook data pid through device_model
#         else:
#             defaultAPI =  APITemplate.TelegramDesktop
#             newClient = TelegramClient(session_name, defaultAPI.api_id, defaultAPI.api_hash, )
        
#         oldClient = self.ToTelethon()

#         await oldClient.connect()
#         await newClient.connect()
#         oldMe = await oldClient.get_me()
        
#         qr_login = await newClient.qr_login()
        
#         try:
#             resp = await oldClient(tl.functions.auth.AcceptLoginTokenRequest(qr_login.token))
#         except BaseException as e:
#             pass

#         try:
#             await qr_login.wait()
#         except telethon.errors.SessionPasswordNeededError as e:

#             # two-step verification
#             username = oldMe.username if (oldMe.username != None) else utils.get_display_name(oldMe)
#             password = input(f"Password for {username}: ")

#             pwd = await newClient(tl.functions.account.GetPasswordRequest())
#             result = await newClient(tl.functions.auth.CheckPasswordRequest(
#                 pwd_mod.compute_check(pwd, password)))
        
#             newClient._on_login(result.user)

#         await newClient.get_me()
#         return newClient
