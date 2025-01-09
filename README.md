# ROS 2 DatetimeTalkerで現在日時を取得
このROS 2パッケージは、DatetimeTalkerノードを使用して、システムの現在日時を定期的にパブリッシュします。
### 概要
DatetimeTalker: 毎秒現在日時を取得してパブリッシュします。

DatetimeListener: 受信した日時を端末に出力します。
#### ノードを実行する
DatetimeTalkerとDatetimeListenerを起動するには以下を使用します。
```
ros2 launch mypkg datetime_talk_listen.launch.py
```
### 実行例
以下はDatetimeTalkerとDatetimeListenerの実行例です：
```
[datetime_talker]: Published: 現在の日時: 2025-01-04 16:07:23
[datetime_listener]: Listen: 現在の日時: 2025-01-04 16:07:23
```
### 動作環境
Ubuntu 22.04 LTS

ROS 2 (Humble以降)

Python 3.8以上
#### ライセンス
このリポジトリはBSD-3-Clauseライセンスのもとで公開されています。
#### Copyright
© 2025 Daichi Hirose
