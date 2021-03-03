import Scale from './Scale';
import IntervalScale from './Interval';
import List from '../data/List';
import { DimensionName, ScaleTick } from '../util/types';
declare class LogScale extends Scale {
    static type: string;
    readonly type = "log";
    base: number;
    private _originalScale;
    private _fixMin;
    private _fixMax;
    private _interval;
    private _niceExtent;
    getTicks(expandToNicedExtent: boolean): ScaleTick[];
    setExtent(start: number, end: number): void;
    getExtent(): [number, number];
    unionExtent(extent: [number, number]): void;
    unionExtentFromData(data: List, dim: DimensionName): void;
    niceTicks(approxTickNum: number): void;
    niceExtent(opt: {
        splitNumber: number;
        fixMin?: boolean;
        fixMax?: boolean;
        minInterval?: number;
        maxInterval?: number;
    }): void;
    parse(val: any): number;
    contain(val: number): boolean;
    normalize(val: number): number;
    scale(val: number): number;
    getMinorTicks: IntervalScale['getMinorTicks'];
    getLabel: IntervalScale['getLabel'];
}
export default LogScale;