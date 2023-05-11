solutions = [
  { "name"        : "src/electron",
    "url"         : "https://github.com/Dragon-S/electron.git@b81432852ad80812216ee4dc8c57ed716bd4263e",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {
      "src/third_party/webrtc": "https://github.com/Dragon-S/google-webrtc.git@59519cbd47f31cbd55b54aea3dff06ed68f19b2e",
    },
    "custom_vars": {},
  },
]