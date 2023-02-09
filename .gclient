solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@3dd15aec62dfff5f7cc9c0c5d17a72358a8d63b5",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@d74d1529df5abc0c13ad4d56b0056837b1ba4b61",
    },
    "custom_vars": {},
  },
]