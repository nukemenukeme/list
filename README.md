# list

 - 基本は作家名のアルファベット順で表示させる。
 - 国別、作品ジャンル別、グループ名でも探せるできるようにする。
 - ベーシック認証をかける。
 - 画像版で、タグクラウドで画像管理できるものもそのうち作る
 
## やりたいこと色々

 - ベーシック認証をかけて、resisterでアカウント登録
 - トップページにランダムで、1人だけアーティスト名とリンクが表示されるようにする
 - A~Zのアルファベット毎にまとめて、先頭に"A"とか"G"とかつける (参考: http://bb9.berlinbiennale.de/participants/ )
 - アルファベットを入力すると、その頭文字で始まるアーティスト名が返ってくる
 - 日本名の場合、読みがなをつける
 - Tagsを選ぶと、選んだTags以外の名前が薄く消えるようにする、もしくはdisplay:noneになるようにする
 - Indexを3列表示にする
 - スプレッドシートから自動更新されるようにする
 - profileの書式は{{ profile }} (via {{ source.link }})にする
