solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@7fb878eab9524e89af95f6e1d79d3af27989133b",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@d74d1529df5abc0c13ad4d56b0056837b1ba4b61",
    },
    "custom_vars": {},
  },
]