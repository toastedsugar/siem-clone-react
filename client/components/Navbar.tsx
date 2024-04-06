"use client";

import Link from "next/link";
import { useContext, useEffect } from "react";

import ThemeSwitch from "./ThemeSwitch";

export default function Navbar() {
  return (
    <nav className="flex flex-row justify-center items-center gap-16 bg-zinc-200 dark:bg-zinc-800 text-xl p-2">
      <ThemeSwitch />
      <Link href="/dashboard">
        <button>Dashboard</button>
      </Link>
      <Link href="/about">
        <button>About</button>
      </Link>
    </nav>
  );
}
