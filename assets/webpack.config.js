const path = require('path');
const webpack = require('webpack');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const TerserJSPlugin = require('terser-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');


module.exports = {
    mode: 'development',
    entry: ['./src/js/index.js', './src/css/base.scss'],

    output: {
        filename: 'app.js',
        path: path.resolve(__dirname, '..', 'server', 'pfchar', 'static')
    },

    plugins: [new webpack.ProgressPlugin(), new CleanWebpackPlugin(), new MiniCssExtractPlugin({
        filename: 'styles.css',
        path: path.resolve(__dirname, '..', 'server', 'pfchar', 'static')
    })],

    module: {
        rules: [
            {
                test: /.(js|jsx)$/,
                include: [path.resolve(__dirname, 'src')],
                loader: 'babel-loader',

                options: {
                    plugins: ['syntax-dynamic-import'],

                    presets: [
                        [
                            '@babel/preset-env',
                            {
                                modules: false
                            }
                        ]
                    ]
                }
            }, {
                test: /\.scss$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader']
            }
        ]
    },

    optimization: {
        minimizer: [new TerserJSPlugin({}), new OptimizeCSSAssetsPlugin({})]
    },

    devServer: {
        open: true
    }
};
