・作ろうとした理由

同じコメントをしている人物を、複数のニュースで存在しないか確認したかったため。

・苦労した点

yahooのコメント欄はjavascriptで出力しているため、通常のスクレイピングができず、seleniumによって情報取得する道を取らざるを得なかった。
また、javascriptに対応したコードを書いても情報を取得できるときとできないときがあった。それは、ブラウザが開いてコメントが表示されるまでにコードが先んじて取得しようとしてエラーになっていたから。そのためコメントが現れるまでtime.sleep関数を使って情報取得するコードを待機させるように工夫した。


