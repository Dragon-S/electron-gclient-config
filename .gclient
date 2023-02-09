solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@45d933fceb713ed302e2b416faa66b085b8a036b",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@b3f11abe4089298435f1a0035e1c62378f55f4a6",
    },
    "custom_vars": {},
  },
]