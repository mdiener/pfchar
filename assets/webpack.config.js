const path = require('path');
const webpack = require('webpack');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const TerserJSPlugin = require('terser-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');


var config = {
};


var jsConfig = Object.assign({}, config, {
    entry: {
        characters: path.resolve(__dirname, 'src', 'js', 'characters.js'),
        character: path.resolve(__dirname, 'src', 'js', 'character.js')
    },

    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, '..', 'server', 'pfchar', 'static')
    },

    plugins: [new webpack.ProgressPlugin()],

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
            }
        ]
    },

    optimization: {
        minimizer: [new TerserJSPlugin({})]
    },

    devServer: {
        open: true
    }
});

var cssConfig = Object.assign({}, config, {
    // entry: path.resolve(__dirname, 'src', 'css', 'base.scss'),
    entry: {
        styles: path.resolve(__dirname, 'src', 'css', 'base.scss')
    },

    output: {
        // filename: 'styles.js',
        path: path.resolve(__dirname, '..', 'server', 'pfchar', 'static')
    },

    plugins: [new MiniCssExtractPlugin({
        filename: 'styles.css',
        path: path.resolve(__dirname, '..', 'server', 'pfchar', 'static')
    })],

    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader']
            }
        ]
    },

    optimization: {
        minimizer: [new OptimizeCSSAssetsPlugin({})]
    }
})


module.exports = [jsConfig, cssConfig];
