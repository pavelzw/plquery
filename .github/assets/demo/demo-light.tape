Output .github/assets/demo/demo-light.mp4
Output .github/assets/demo/demo-light.gif

Set Theme "rose-pine-dawn"
Set Shell "bash"
Set FontSize 32
Set Width 1920
Set Height 750

Hide
Type "pixi shell" Enter
Sleep 1s
Type "cd ./examples" Enter
Type "clear" Enter
Sleep 1s
Show

Type@150ms "plquery df.parquet" Sleep 1s Enter
Sleep 3s

Type@150ms "df" Sleep 1s Enter
Sleep 3s

Type@150ms '.select(pl.col("foo") * 2)' Sleep 1s Enter
Sleep 10s
