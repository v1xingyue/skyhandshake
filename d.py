from namebase.dns import status, markTXT, getNsServer

# print(status("vul"))

print(getNsServer("vul"))
print(markTXT("vul", "hello.world.", "HAFyYkiBD-vCCCYnwDKC2dgaJEblMXfZ1BhYEKOClMkxUg"))
