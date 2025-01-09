# mypkg
### パッケージ概要
このROS 2パッケージは、`battery_talker.py`ノードを使用して、毎秒端末のバッテリー状況を表示します。
### ノード概要
`battery_talker.py`<br>毎秒端末のバッテリー状況を取得します。<br>取得したデータを`battery_status`トピックにパブリッシュします。

`battery_listener.py`<br>テスト用
### 使用方法
#### ノードの起動とデータの確認
`battery_talker.py`の実行
```
ros2 run mypkg battery_talker
```
#### データの確認
別の端末で以下を実行し、トピックのデータを表示します。
```
ros2 topic echo /battery_status
```
#### 出力例
```
data: 94.0%
---
data: 94.0%
---
data: 94.0%
---
data: 94.0%
---
data: 94.0%
```
### 動作環境
Ubuntu 22.04 LTS

ROS 2 (Humble以降)

Python 3.8以上
#### ライセンス
このリポジトリは3条項BSDライセンスの下で公開されています。<br>詳細はLICENSEをご確認ください。
#### Copyright
© 2025 Daichi Hirose
