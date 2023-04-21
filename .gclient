solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@b92295e2e84d29637714ef2250babe6f108ca1d5",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@59519cbd47f31cbd55b54aea3dff06ed68f19b2e",
    },
    "custom_vars": {},
  },
]