solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@53b50f2abb0bd46afe4832fd1be68a2b67723d77",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@08067eabee69c8b70c2409657a42224fdc6a1a23",
    },
    "custom_vars": {},
  },
]