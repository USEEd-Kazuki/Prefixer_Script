## Unreal Engine <br /> アセットタイプ自動追加スクリプト
このスクリプトは、Unreal Engine 内の選択したアセットに対して、指定されたクラスタイプを自動的に追加します。

## 使い方
<br />1 , prefix_mapping.json ファイルを編集し、各クラスに対応するプレフィックスを指定します。
<br />    JSON ファイルの例は以下の通りです:
<br />      {
<br />      "StaticMesh": "SM_",
<br />      "Material": "M_",
<br />      "Texture2D": "T_"
<br />      }
<br />2 , Unreal Engine 内でスクリプトを実行します。
<br />    スクリプトは選択したアセットに対してアセットタイプを追加し、その結果をログに出力します。

## インストール
<br />このスクリプトをUnreal Engineプロジェクトに組み込むには、以下の手順を実行してください：
<br />1 , Content/Scripts や適切なディレクトリにPythonスクリプトを配置します。
<br />2 , Unreal Engine内でPythonスクリプトを実行します。

## 注意事項
- スクリプトを実行する前に、prefix_mapping.json ファイルを適切に編集してください。
- このスクリプトを使用する前に、変更されるアセットのバックアップを作成することをお勧めします。

## 作者
UESSd-Kazuki
