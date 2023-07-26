<?php

// 获取图片主题色的函数
function getImageThemeColor($imageUrl) {
    // 读取图片文件
    $image = imagecreatefromstring(file_get_contents($imageUrl));
    
    // 调整图片大小为1x1像素
    $thumbnail = imagecreatetruecolor(1, 1);
    imagecopyresampled($thumbnail, $image, 0, 0, 0, 0, 1, 1, imagesx($image), imagesy($image));
    
    // 获取像素的RGB值
    $rgb = imagecolorat($thumbnail, 0, 0);
    $r = ($rgb >> 16) & 0xFF;
    $g = ($rgb >> 8) & 0xFF;
    $b = $rgb & 0xFF;
    
    // 转换为指定格式
    $color = sprintf("#%02x%02x%02x", $r, $g, $b);
    
    // 返回RGB值
    return $color;
}

/// 检查是否传入图片URL参数
if (isset($_GET['img'])) {
    $imageUrl = $_GET['img'];

    // 检查是否已经存在对应链接的色彩信息
    $jsonFile = 'colors.json';
    $colors = array();

    if (file_exists($jsonFile)) {
        $json = file_get_contents($jsonFile);
        $colors = json_decode($json, true);
    }

    // 检查是否已经存储了对应链接的色彩信息
    if (isset($colors[$imageUrl])) {
        // 直接读取已存储的色彩信息并输出
        $themeColor = $colors[$imageUrl];
        echo $themeColor; // 输出主题色值
    } else {
        // 获取图片主题色
        $themeColor = getImageThemeColor($imageUrl);

        // 将色彩信息存储到数组中
        $colors[$imageUrl] = $themeColor;

         // 输出主题色值
        echo $themeColor;
    }
} else {
    // 如果未传入img参数，则返回错误信息
    echo '错误，请在URL中加上?img=';
}
?>
