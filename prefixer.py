import unreal
import json

editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

#prefix mapping
prefix_mapping = {}

# jsoファイルパスを指定して読み込み
with open("Y:\\Desktop\\Prefixer_Script\\prefix_mapping.json", "r") as json_file:
    # JSONファイルを読み込んでディクショナリにパース
    prefix_mapping = json.loads(json_file.read())

# 選択中のアセットを取得
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
prefixed = 0

for asset in selected_assets:

    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)
    
    # get the prefix for the given class
    class_prefix = prefix_mapping.get(class_name, None)

    if class_prefix is None:
        # 警告をログに出力して、マッピングが存在しないことを通知
        unreal.log_warning("No mapping for asset {} of type {}".format(asset_name, class_name))
        continue

    if not asset_name.startswith(class_prefix):
        # アセットの名前を変更し、prefixを追加
        new_name = class_prefix + asset_name
        editor_util.rename_asset(asset, new_name)
        prefixed += 1
        unreal.log("Prefixed {} of type {} with {}".format(asset_name, class_name, class_prefix))

    # prefixが追加されたアセットの数と選択されたアセットの総数をログに出力
    unreal.log("{} with class {}".format(prefixed, num_assets))