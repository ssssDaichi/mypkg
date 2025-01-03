import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    talker = launch_ros.actions.Node(
        package='mypkg',         # パッケージ名
        executable='talker',     # 実行するノード名
    )
    listener = launch_ros.actions.Node(
        package='mypkg',         # パッケージ名
        executable='listener',   # 実行するノード名
        output='screen',         # ログを端末に出力
    )

    return launch.LaunchDescription([talker, listener])
