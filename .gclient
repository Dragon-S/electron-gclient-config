solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@18fc04471b467320019671dbf250dc46e1679296",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@b0c7a6bc9d363aa05e0181e91502f9aa51f316fd",
    },
    "custom_vars": {},
  },
]