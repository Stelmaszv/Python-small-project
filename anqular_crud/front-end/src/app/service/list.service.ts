import { Injectable } from '@angular/core';
import {Observable} from 'rxjs'
import { HttpClient,HttpHeaders } from '@angular/common/http'
import { List_Model } from '../model/list'

@Injectable({
  providedIn: 'root'
})
export class ListService {
  list:string = 'http://127.0.0.1:8000/list/';
  limit = '?_limit=5';
  constructor(private http:HttpClient) { }
  getList() :Observable<List_Model[]> {
      return this.http.get<List_Model[]>(this.list)
  }
  get(id) :Observable<List_Model[]>{
    const url=`${this.list}${id}`
    return this.http.get<List_Model[]>(url)
  }
  add(form){
    this.http.post(this.list,form).subscribe(item => {
      console.log(item)
    });
  }
}
