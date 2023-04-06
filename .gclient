solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@b4bb2521ab102f6ca041dff6093aa3a667dd53ec",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@59519cbd47f31cbd55b54aea3dff06ed68f19b2e",
    },
    "custom_vars": {},
  },
]