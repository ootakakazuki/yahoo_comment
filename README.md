・作ろうとした理由  
  
同じコメントをしている人物を、複数のニュースで存在しないか確認したかったため。  
  
・苦労した点  
  
yahooのコメント欄はjavascriptで出力しているため、通常のスクレイピングができず、seleniumによって情報取得する道を取らざるを得なかった。  
また、javascriptに対応したコードを書いても情報を取得できるときとできないときがあった。  
それは、ブラウザが開いてコメントが表示されるまでにコードが先んじて取得しようとしてエラーになっていたから。  
そのためコメントが現れるまでtime.sleep関数を使って情報取得するコードを待機させるように工夫した。  
  
【実行】  
`python3 selenium_pra.py`  
で実行したあと、読み込むページ数と、urlを入力する。  
urlは下記のように、最後は`/comments?page＝`の形にする  
  
https://news.yahoo.co.jp/articles/a711c97aac141f8892991acd61c86e94c612dcbe/comments?page=  
  
5ページ分(つまり50コメント)の場合は  
  
`python3 selenium_pra.py`(エンター)  
5 (エンター)  
https://news.yahoo.co.jp/articles/a711c97aac141f8892991acd61c86e94c612dcbe/comments?page=  (エンター)  
  
とする。  


